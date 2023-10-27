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


insn_tab = {}
with open("./insn.json", "r") as f:
    insn_tab = json.load(f)

tplt_func_sig = """[__POUT__] [__FUNC_NAME__] ([__P_IN__]);"""
instrinsic_names = {}
print(f"|insn|type|extension|intrinsics|status|rv32 testsuite|rv64 testsuite|")
print(f"|---|---|---|---|---|---|---|")
for insn in insn_tab['insns']:
    if 'intrinsics' not in insn:
        continue
    n = insn['insn']
    ext = re.findall(r"^([zpn|zpsfoperand|zbpbo]+)[\d]*$",  insn['extension'])[0]
    intrinsic_str_both = []
    intrinsic_str_rv32 = []
    intrinsic_str_rv64 = []
    for j, insc in enumerate(insn['intrinsics']):
        xlen = insc['xlen']
        insn_name = insc['name'][5:]
        p_out = insc['types'][0]
        p_in = []
        for i, p in enumerate(insc['types'][1:]):
            p_in.append(f"{p} x{i}")
        p_in = ", ".join(p_in)
        
        nn = f"__rv_{insn_name}"
        func_str = tplt_func_sig.replace("[__FUNC_NAME__]", nn)
        if nn not in instrinsic_names:
            instrinsic_names[nn] = len(insc['types'][1:])
        
        func_str = func_str.replace("[__POUT__]", p_out)
        func_str = func_str.replace("[__P_IN__]", p_in)

        if xlen == '*':# need to generate both of rv32 and rv64.
            intrinsic_str_both.append(func_str)         
        elif xlen == '32':
            intrinsic_str_rv32.append(func_str)
        elif xlen == '64':
            intrinsic_str_rv64.append(func_str)
    if len(intrinsic_str_both) > 0:
        intrinsic_str_both = "rv32 and rv64: <br />" + "<br />".join(intrinsic_str_both)
    else:
        intrinsic_str_both = ""
    if len(intrinsic_str_rv32):
        intrinsic_str_rv32 = "rv32 only: <br />" + "<br />".join(intrinsic_str_rv32)
    else:
        intrinsic_str_rv32 = ""
    if len(intrinsic_str_rv64):
        intrinsic_str_rv64 = "rv32 only: <br />" + "<br />".join(intrinsic_str_rv64)
    else:
        intrinsic_str_rv64 = ""
    intrinsic_str = "<br />".join([intrinsic_str_both, intrinsic_str_rv32,intrinsic_str_rv64])
    
    print(f"|{n}|{insn['type']}|{ext}|{intrinsic_str}|done|<span style=\"color:green\">success</span>|<span style=\"color:green\">success</span>|")