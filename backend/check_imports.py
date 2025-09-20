#!/usr/bin/env python3
"""
Comprehensive import checker for the healthcare diagnosis backend.
This script attempts to import all modules and reports which ones fail.
"""

import sys
import os
import importlib
from pathlib import Path

def find_python_modules(src_path):
    """Find all Python modules in the src directory."""
    modules = []
    src_path = Path(src_path)
    
    for py_file in src_path.rglob("*.py"):
        if py_file.name == "__init__.py":
            # For __init__.py files, use the parent directory name
            rel_path = py_file.parent.relative_to(src_path)
            if str(rel_path) != ".":
                module_name = str(rel_path).replace(os.sep, ".")
                modules.append(f"src.{module_name}")
        else:
            # For regular .py files
            rel_path = py_file.relative_to(src_path)
            module_name = str(rel_path.with_suffix("")).replace(os.sep, ".")
            modules.append(f"src.{module_name}")
    
    return sorted(set(modules))

def test_imports():
    """Test importing all modules and report failures."""
    src_path = Path(__file__).parent / "src"
    modules = find_python_modules(src_path)
    
    print("🔍 HEALTHCARE DIAGNOSIS BACKEND - IMPORT ANALYSIS")
    print("=" * 60)
    
    successful_imports = []
    failed_imports = []
    
    for module in modules:
        try:
            importlib.import_module(module)
            successful_imports.append(module)
            print(f"✅ {module}")
        except Exception as e:
            failed_imports.append((module, str(e)))
            print(f"❌ {module}: {e}")
    
    print(f"\n📊 SUMMARY:")
    print(f"✅ Successful imports: {len(successful_imports)}")
    print(f"❌ Failed imports: {len(failed_imports)}")
    
    if failed_imports:
        print(f"\n🚨 FAILED IMPORTS DETAILS:")
        for module, error in failed_imports:
            print(f"  • {module}")
            print(f"    Error: {error}")
            print()
    
    return len(failed_imports) == 0

if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)