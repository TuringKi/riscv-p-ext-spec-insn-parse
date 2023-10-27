#
# MIT License
# Copyright (c) 2023 mxlol233 (mxlol233@outlook.com)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#


tplt_file = """/* This is a test program for [__INSN__] instruction.  */
/* { dg-do compile { target riscv[__XLEN__]*-*-* } } */
/* { dg-options "-march=rv[__XLEN__]gc_[__EXT__] -mabi=[__ABI__] -O[__OPT_LEVEL__]" } */
/* { dg-final { check-function-bodies "**" "" "" } } */

#include <rvp_intrinsic.h>

[__FUNC__]


"""

tplt_func = """
/*
**[__FUNC_NAME__]:
** [___ASM__]
** ...
*/

[__POUT__] [__FUNC_NAME__] ([__P_IN__]){

    return __rv_[__INSN__]([__PS__]);

}
"""

insn_tab = {}
with open("/root/plctlab/proj1/gcc/rvp_insn.json", "r") as f:
    insn_tab = json.load(f)

save_root = "/root/gcc/gcc/testsuite/gcc.target/riscv/"
func_idx = 0
for insn in insn_tab['insns']:
    if 'intrinsics' not in insn:
        continue
    n = insn['insn']
    opt_level = "3"
    if "opt_level" in insn:
        opt_level = insn['opt_level']
    file_str_ = tplt_file.replace("[__OPT_LEVEL__]", opt_level)
    ext = re.findall(r"^([zpn|zpsfoperand|zbpbo]+)[\d]*$",  insn['extension'])[0]
    scane_times = len(insn['intrinsics']) + 1
    if ext == 'zpn':
        file_str_ = file_str_.replace("[__EXT__]", ext)
    else:
        file_str_ = file_str_.replace("[__EXT__]", "zpn_" + ext)
    file_str_ = file_str_.replace("[__INSN__]", n)
    funcs_str_32 = []
    funcs_str_64 = []
    
    for j, insc in enumerate(insn['intrinsics']):
        xlen = insc['xlen']
        insn_name = insc['name'][5:]
        p_out = insc['types'][0]
        p_in = []
        
        def_in_param = []
        for i, (p, is_imm) in enumerate(zip(insc['types'][1:], insc['is_imm'][1:])):
            #if is_imm == 'N':    
            p_in.append(f"{p} x{i}")
            def_in_param.append(f"{p}")
            #else:
            #    def_in_param.append(f"const {p}")
        p_in = ", ".join(p_in)
        def_str = ""
        if insn_name.startswith("v"):
            def_str = "CREATE_RVP_INTRINSIC_VECTOR(" + ", ".join([p_out, insn_name[2:], *def_in_param]) +")"
        else:
            def_str = "CREATE_RVP_INTRINSIC(" + ", ".join([p_out, insn_name, *def_in_param]) +")"
        func_str = tplt_func.replace("[__FUNC_NAME__]", f"f{j}")
        func_str = func_str.replace("[__INSN__]", insn_name)
        func_str = func_str.replace("[__POUT__]", p_out)
        func_str = func_str.replace("[__P_IN__]", p_in)
        in_param = []
        asm_ss = []
        has_imm = False
        for i, (p, is_imm) in enumerate(zip(insc['types'][1:], insc['is_imm'][1:])):
            if is_imm == 'Y':
                asm_ss.append("1")
                in_param.append("1")
                has_imm = True
            else:
                asm_ss.append("a[0-9]")
                in_param.append(f"x{i}")
        
        func_str = func_str.replace("[__PS__]", ", ".join(in_param))
        asm_n = n
        
        if 'asm' in insc:
            asm_str = insc['asm']
        else:
            asm_str = ""
            if opt_level == '0':
                asm_str = "...\n"
            
            if "alias" in insn:
                asm_n = insn['alias']
            if insc['n_operand'] == len(asm_ss) + 1:
                asm_str += f"{asm_n}\\t" + ",".join(["a[0-9]", *asm_ss])
            else:
                if not has_imm:
                    asm_str += f"{asm_n}\\t" + ",".join(["a[0-9]" for _ in range(insc['n_operand']) ])
                else:
                    asm_str += f"{asm_n}\\t" + ",".join(["a[0-9]" for _ in range(insc['n_operand'] -1) ]) + ",1"
        func_str = func_str.replace("[___ASM__]", asm_str)
        if xlen == '*':# need to generate both of rv32 and rv64.
            funcs_str_32.append(func_str)
            funcs_str_64.append(func_str)        
        elif xlen == '32':
            funcs_str_32.append(func_str)
        elif xlen == '64':
            funcs_str_64.append(func_str)
        
    
    if len(funcs_str_32)>0:
        file_str = file_str_
        save_path = f"{save_root}/rvp32/builtin-rvp32-{n}.c"
        file_str = file_str.replace("[__SCAN_TIMES__]", f"{len(funcs_str_32) + 1}")
        file_str = file_str.replace("[__XLEN__]", "32")
        file_str = file_str.replace("[__ABI__]", "ilp32d")
        file_str = file_str.replace("[__FUNC__]", "\n\n".join(funcs_str_32))
      
        with open(save_path, "w") as f:
            f.write(file_str)
            
    
    if len(funcs_str_64)>0:
        file_str = file_str_
        save_path = f"{save_root}/rvp64/builtin-rvp64-{n}.c"
        file_str = file_str.replace("[__SCAN_TIMES__]", f"{len(funcs_str_64) + 1}")
        file_str = file_str.replace("[__XLEN__]", "64")
        file_str = file_str.replace("[__ABI__]", "lp64d")
        file_str = file_str.replace("[__FUNC__]", "\n\n".join(funcs_str_64))

        with open(save_path, "w") as f:
            f.write(file_str)
    
