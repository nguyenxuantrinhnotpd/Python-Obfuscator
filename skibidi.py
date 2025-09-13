#!/usr/bin/env python3
"""
Python Code Obfuscator - Chuyển đổi code Python thành dạng state machine

Công cụ này sẽ biến đổi code Python thành một dạng khó đọc bằng cách:
- Sử dụng ký tự Hàn Quốc làm tên biến
- Chuyển đổi luồng thực thi thành state machine với while loop
- Xáo trộn thứ tự các case để làm khó hiểu logic

Author: NGUYEN XUAN TRINH
"""

import ast
import random
import argparse
import sys
import os
from pathlib import Path


class PythonObfuscator:
    """Lớp chính để obfuscate Python code"""
    
    def __init__(self, use_korean_chars=True, random_seed=None):
        """
        Khởi tạo obfuscator
        
        Args:
            use_korean_chars (bool): Sử dụng ký tự Hàn Quốc cho tên biến
            random_seed (int): Seed cho random generator (để có kết quả nhất quán)
        """
        self.use_korean_chars = use_korean_chars
        if random_seed is not None:
            random.seed(random_seed)
    
    def generate_variable_name(self, length=20):
        """Tạo tên biến ngẫu nhiên"""
        if self.use_korean_chars:
            chars = [chr(random.randint(44032, 55203)) for _ in range(length)]
            return ''.join(chars)
        else:
            # Sử dụng ký tự Latin nếu không muốn dùng Hàn Quốc
            chars = [chr(random.randint(97, 122)) for _ in range(length)]
            return 'var_' + ''.join(chars)
    
    def obfuscate(self, source_code: str) -> str:
        """
        Obfuscate Python code
        
        Args:
            source_code (str): Mã nguồn Python cần obfuscate
            
        Returns:
            str: Mã đã được obfuscate
        """
        try:
            tree = ast.parse(source_code)
        except SyntaxError as e:
            raise ValueError(f"Lỗi cú pháp trong mã nguồn: {e}")
        
        stmts = tree.body
        pc_var = self.generate_variable_name()
        
        if not stmts:
            return f'{pc_var} = 0\n# Không có câu lệnh nào để obfuscate'
        
        n = len(stmts)
        random_offset = random.randint(1, 1000000000000)
        labels = list(range(random_offset, random_offset + n))
        end_label = random_offset + n
        
        match_cases = []
        
        for i, (lbl, node) in enumerate(zip(labels, stmts)):
            next_pc = end_label if i == n - 1 else labels[i + 1]
            case_body = []
            
            if isinstance(node, ast.stmt):
                case_body.append(node)
            else:
                case_body.extend(node)
            
            pc_assign = ast.Assign(
                targets=[ast.Name(id=pc_var, ctx=ast.Store())], 
                value=ast.Constant(value=next_pc)
            )
            case_body.append(pc_assign)
            
            match_case = ast.match_case(
                pattern=ast.MatchValue(value=ast.Constant(value=lbl)), 
                guard=None, 
                body=case_body
            )
            match_cases.append(match_case)
        
        # Xáo trộn thứ tự các case
        random.shuffle(match_cases)
        
        # Thêm case kết thúc
        match_cases.append(ast.match_case(
            pattern=ast.MatchValue(value=ast.Constant(value=end_label)), 
            guard=None, 
            body=[ast.Break()]
        ))
        
        # Thêm case mặc định
        match_cases.append(ast.match_case(
            pattern=ast.MatchAs(), 
            guard=None, 
            body=[ast.Break()]
        ))
        
        # Tạo match statement
        match_stmt = ast.Match(
            subject=ast.Name(id=pc_var, ctx=ast.Load()), 
            cases=match_cases
        )
        
        # Tạo while loop
        while_loop = ast.While(
            test=ast.Constant(value=True), 
            body=[match_stmt], 
            orelse=[]
        )
        
        # Khởi tạo PC
        init_pc = ast.Assign(
            targets=[ast.Name(id=pc_var, ctx=ast.Store())], 
            value=ast.Constant(value=labels[0] if labels else 0)
        )
        
        # Tạo module mới
        module = ast.Module(body=[init_pc, while_loop], type_ignores=[])
        ast.fix_missing_locations(module)
        
        return ast.unparse(module)


def main():
    """Hàm main để chạy từ command line"""
    parser = argparse.ArgumentParser(
        description="Python Code Obfuscator - Obfuscate mã Python bằng state machine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ sử dụng:
  python skibidi.py input.py                    # Obfuscate và in ra màn hình
  python skibidi.py input.py -o output.py      # Obfuscate và lưu vào file
  python skibidi.py input.py -r                # Chạy code đã obfuscate
  python skibidi.py input.py --no-korean       # Không sử dụng ký tự Hàn Quốc
  python skibidi.py input.py --seed 123        # Sử dụng seed cố định
        """
    )
    
    parser.add_argument(
        'input_file', 
        help='File Python cần obfuscate'
    )
    
    parser.add_argument(
        '-o', '--output', 
        help='File đầu ra (mặc định: in ra màn hình)'
    )
    
    parser.add_argument(
        '-r', '--run', 
        action='store_true',
        help='Chạy code đã obfuscate sau khi tạo'
    )
    
    parser.add_argument(
        '--no-korean', 
        action='store_true',
        help='Không sử dụng ký tự Hàn Quốc cho tên biến'
    )
    
    parser.add_argument(
        '--seed', 
        type=int,
        help='Seed cho random generator (để có kết quả nhất quán)'
    )
    
    parser.add_argument(
        '-v', '--verbose', 
        action='store_true',
        help='In thông tin chi tiết'
    )
    
    args = parser.parse_args()
    
    # Kiểm tra file input
    if not os.path.exists(args.input_file):
        print(f"❌ Lỗi: File '{args.input_file}' không tồn tại!", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Đọc file input
        if args.verbose:
            print(f"📖 Đang đọc file: {args.input_file}")
        
        with open(args.input_file, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        # Tạo obfuscator
        obfuscator = PythonObfuscator(
            use_korean_chars=not args.no_korean,
            random_seed=args.seed
        )
        
        # Obfuscate code
        if args.verbose:
            print("🔄 Đang obfuscate code...")
        
        obfuscated_code = obfuscator.obfuscate(source_code)
        
        # Xuất kết quả
        if args.output:
            if args.verbose:
                print(f"💾 Đang lưu vào file: {args.output}")
            
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(obfuscated_code)
            
            print(f"✅ Đã obfuscate thành công! Kết quả lưu tại: {args.output}")
        else:
            print("=" * 60)
            print("OBFUSCATED CODE:")
            print("=" * 60)
            print(obfuscated_code)
            print("=" * 60)
        
        # Chạy code nếu được yêu cầu
        if args.run:
            if args.verbose:
                print("🚀 Đang chạy code đã obfuscate...")
            print("\n" + "=" * 40)
            print("OUTPUT:")
            print("=" * 40)
            exec(obfuscated_code)
            
    except FileNotFoundError:
        print(f"❌ Lỗi: Không thể đọc file '{args.input_file}'!", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"❌ Lỗi: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Lỗi không mong muốn: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':

    main()
