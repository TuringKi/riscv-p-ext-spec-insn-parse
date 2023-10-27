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


import regex as re
import json

all_rv = """|1 |ADD8 |1 |1
|2 |ADD16 |1 |1
|3 |ADD64 |1 |1
|4 |AVE |1 |1
|5 |BITREV |1 |1
|6 |BITREVI |1 |1
|7 |BPICK |1 |1
|8 |CLROV |1 |1
|9 |CLRS8 |1 |1
|10 |CLRS16 |1 |1
|11 |CLRS32 |1 |1
|12 |CLZ8 |1 |1
|13 |CLZ16 |1 |1
|14 |CLZ32 |1 |1
|15 |CMPEQ8 |1 |1
|16 |CMPEQ16 |1 |1
|17 |CRAS16 |1 |1
|18 |CRSA16 |1 |1
|19 |INSB |1 |1
|20 |KABS8 |1 |1
|21 |KABS16 |1 |1
|22 |KABSW |1 |1
|23 |KADD8 |1 |1
|24 |KADD16 |1 |1
|25 |KADD64 |1 |1
|26 |KADDH |1 |1
|27 |KADDW |1 |1
|28 |KCRAS16 |1 |1
|29 |KCRSA16 |1 |1
|30 |KDMBB |1 |1
|31 |KDMBT |1 |1
|32 |KDMTT |1 |1
|33 |KDMABB |2 |1
|34 |KDMABT |2 |1
|35 |KDMATT |2 |1
|36 |KHM8 |1 |1
|37 |KHMX8 |1 |1
|38 |KHM16 |1 |1
|39 |KHMX16 |1 |1
|40 |KHMBB |1 |1
|41 |KHMBT |1 |1
|42 |KHMTT |1 |1
|43 |KMABB |2 |1
|44 |KMABT |2 |1
|45 |KMATT |2 |1
|46 |KMADA |2 |1
|47 |KMAXDA |2 |1
|48 |KMADS |2 |1
|49 |KMADRS |2 |1
|50 |KMAXDS |2 |1
|51 |KMAR64 |3 |1
|52 |KMDA |2 |1
|53 |KMXDA |2 |1
|54 |KMMAC |2 |1
|55 |KMMAC.u |2 |1
|56 |KMMAWB |2 |1
|57 |KMMAWB.u |2 |1
|58 |KMMAWB2 |2 |1
|59 |KMMAWB2.u |2 |1
|60 |KMMAWT |2 |1
|61 |KMMAWT.u |2 |1
|62 |KMMAWT2 |2 |1
|63 |KMMAWT2.u |2 |1
|64 |KMMSB |2 |1
|65 |KMMSB.u |2 |1
|66 |KMMWB2 |2 |1
|67 |KMMWB2.u |2 |1
|68 |KMMWT2 |2 |1
|69 |KMMWT2.u |2 |1
|70 |KMSDA |2 |1
|71 |KMSXDA |2 |1
|72 |KMSR64 |3 |1
|73 |KSLLW |1 |1
|74 |KSLLIW |1 |1
|75 |KSLL8 |1 |1
|76 |KSLLI8 |1 |1
|77 |KSLL16 |1 |1
|78 |KSLLI16 |1 |1
|79 |KSLRA8 |1 |1
|80 |KSLRA8.u |1 |1
|81 |KSLRA16 |1 |1
|82 |KSLRA16.u |1 |1
|83 |KSLRAW |1 |1
|84 |KSLRAW.U |1 |1
|85 |KSTAS16 |1 |1
|86 |KSTSA16 |1 |1
|87 |KSUB8 |1 |1
|88 |KSUB16 |1 |1
|89 |KSUB64 |1 |1
|90 |KSUBH |1 |1
|91 |KSUBW |1 |1
|92 |KWMMUL |2 |1
|93 |KWMMUL.u |2 |1
|94 |MADDR32 |2 |1
|95 |MAXW |1 |1
|96 |MINW |1 |1
|97 |MSUBR32 |2 |1
|98 |MULR64 |2 |1
|99 |MULSR64 |2 |1
|100 |PBSAD |2 |1
|101 |PBSADA |2 |1
|102 |PKBB16 |1 |1
|103 |PKBT16 |1 |1
|104 |PKTT16 |1 |1
|105 |PKTB16 |1 |1
|106 |RADD8 |1 |1
|107 |RADD16 |1 |1
|108 |RADD64 |1 |1
|109 |RADDW |1 |1
|110 |RCRAS16 |1 |1
|111 |RCRSA16 |1 |1
|112 |RDOV |3 |1
|113 |RSTAS16 |1 |1
|114 |RSTSA16 |1 |1
|115 |RSUB8 |1 |1
|116 |RSUB16 |1 |1
|117 |RSUB64 |1 |1
|118 |RSUBW |1 |1
|119 |SCLIP8 |1 |1
|120 |SCLIP16 |1 |1
|121 |SCLIP32 |1 |1
|122 |SCMPLE8 |1 |1
|123 |SCMPLE16 |1 |1
|124 |SCMPLT8 |1 |1
|125 |SCMPLT16 |1 |1
|126 |SLL8 |1 |1
|127 |SLLI8 |1 |1
|128 |SLL16 |1 |1
|129 |SLLI16 |1 |1
|130 |SMAL |3 |1
|131 |SMALBB |3 |1
|132 |SMALBT |3 |1
|133 |SMALTT |3 |1
|134 |SMALDA |3 |1
|135 |SMALXDA |3 |1
|136 |SMALDS |3 |1
|137 |SMALDRS |3 |1
|138 |SMALXDS |3 |1
|139 |SMAR64 |3 |1
|140 |SMAQA |2 |1
|141 |SMAQA.SU |2 |1
|142 |SMAX8 |1 |1
|143 |SMAX16 |1 |1
|144 |SMBB16 |1 |1
|145 |SMBT16 |1 |1
|146 |SMTT16 |1 |1
|147 |SMDS |2 |1
|148 |SMDRS |2 |1
|149 |SMXDS |2 |1
|150 |SMIN8 |1 |1
|151 |SMIN16 |1 |1
|152 |SMMUL |2 |1
|153 |SMMUL.u |2 |1
|154 |SMMWB |2 |1
|155 |SMMWB.u |2 |1
|156 |SMMWT |2 |1
|157 |SMMWT.u |2 |1
|158 |SMSLDA |3 |1
|159 |SMSLXDA |3 |1
|160 |SMSR64 |3 |1
|161 |SMUL8 |1 |1
|162 |SMULX8 |1 |1
|163 |SMUL16 |1 |1
|164 |SMULX16 |1 |1
|165 |SRA.U |1 |1
|166 |SRAI.U |1 |1
|167 |SRA8 |1 |1
|168 |SRA8.u |1 |1
|169 |SRAI8 |1 |1
|170 |SRAI8.u |1 |1
|171 |SRA16 |1 |1
|172 |SRA16.u |1 |1
|173 |SRAI16 |1 |1
|174 |SRAI16.u |1 |1
|175 |SRL8 |1 |1
|176 |SRL8.u |1 |1
|177 |SRLI8 |1 |1
|178 |SRLI8.u |1 |1
|179 |SRL16 |1 |1
|180 |SRL16.u |1 |1
|181 |SRLI16 |1 |1
|182 |SRLI16.u |1 |1
|183 |STAS16 |1 |1
|184 |STSA16 |1 |1
|185 |SUB8 |1 |1
|186 |SUB16 |1 |1
|187 |SUB64 |1 |1
|188 |SUNPKD810 |1 |1
|189 |SUNPKD820 |1 |1
|190 |SUNPKD830 |1 |1
|191 |SUNPKD831 |1 |1
|192 |SUNPKD832 |1 |1
|193 |SWAP8 |1 |1
|194 |SWAP16 |1 |1
|195 |UCLIP8 |1 |1
|196 |UCLIP16 |1 |1
|197 |UCLIP32 |1 |1
|198 |UCMPLE8 |1 |1
|199 |UCMPLE16 |1 |1
|200 |UCMPLT8 |1 |1
|201 |UCMPLT16 |1 |1
|202 |UKADD8 |1 |1
|203 |UKADD16 |1 |1
|204 |UKADD64 |1 |1
|205 |UKADDH |1 |1
|206 |UKADDW |1 |1
|207 |UKCRAS16 |1 |1
|208 |UKCRSA16 |1 |1
|209 |UKMAR64 |3 |1
|210 |UKMSR64 |3 |1
|211 |UKSTAS16 |1 |1
|212 |UKSTSA16 |1 |1
|213 |UKSUB8 |1 |1
|214 |UKSUB16 |1 |1
|215 |UKSUB64 |1 |1
|216 |UKSUBH |1 |1
|217 |UKSUBW |1 |1
|218 |UMAR64 |3 |1
|219 |UMAQA |2 |1
|220 |UMAX8 |1 |1
|221 |UMAX16 |1 |1
|222 |UMIN8 |1 |1
|223 |UMIN16 |1 |1
|224 |UMSR64 |3 |1
|225 |UMUL8 |1 |1
|226 |UMULX8 |1 |1
|227 |UMUL16 |1 |1
|228 |UMULX16 |1 |1
|229 |URADD8 |1 |1
|230 |URADD16 |1 |1
|231 |URADD64 |1 |1
|232 |URADDW |1 |1
|233 |URCRAS16 |1 |1
|234 |URCRSA16 |1 |1
|235 |URSTAS16 |1 |1
|236 |URSTSA16 |1 |1
|237 |URSUB8 |1 |1
|238 |URSUB16 |1 |1
|239 |URSUB64 |1 |1
|240 |URSUBW |1 |1
|241 |WEXTI |1 |1
|242 |WEXT |1 |1
|243 |ZUNPKD810 |1 |1
|244 |ZUNPKD820 |1 |1
|245 |ZUNPKD830 |1 |1
|246 |ZUNPKD831 |1 |1
|247 |ZUNPKD832 |1 |1"""

all_rv64 = """|1 |ADD32 |1 |1
|2 |CRAS32 |1 |1
|3 |CRSA32 |1 |1
|4 |KABS32 |1 |1
|5 |KADD32 |1 |1
|6 |KCRAS32 |1 |1
|7 |KCRSA32 |1 |1
|8 |KDMBB16 |1 |1
|9 |KDMBT16 |1 |1
|10 |KDMTT16 |1 |1
|11 |KDMABB16 |2 |1
|12 |KDMABT16 |2 |1
|13 |KDMATT16 |2 |1
|14 |KHMBB16 |1 |1
|15 |KHMBT16 |1 |1
|16 |KHMTT16 |1 |1
|17 |KMABB32 |3 |1
|18 |KMABT32 |3 |1
|19 |KMATT32 |3 |1
|20 |KMADA32 |3 |1
|21 |KMAXDA32 |3 |1
|22 |KMDA32 |3 |1
|23 |KMXDA32 |3 |1
|24 |KMADS32 |3 |1
|25 |KMADRS32 |3 |1
|26 |KMAXDS32 |3 |1
|27 |KMSDA32 |3 |1
|28 |KMSXDA32 |3 |1
|29 |KSLL32 |1 |1
|30 |KSLLI32 |1 |1
|31 |KSLRA32 |1 |1
|32 |KSLRA32.u |1 |1
|33 |KSTAS32 |1 |1
|34 |KSTSA32 |1 |1
|35 |KSUB32 |1 |1
|36 |PKBB32 |1 |1
|37 |PKBT32 |1 |1
|38 |PKTB32 |1 |1
|39 |PKTT32 |1 |1
|40 |RADD32 |1 |1
|41 |RCRAS32 |1 |1
|42 |RCRSA32 |1 |1
|43 |RSTAS32 |1 |1
|44 |RSTSA32 |1 |1
|45 |RSUB32 |1 |1
|46 |SLL32 |1 |1
|47 |SLLI32 |1 |1
|48 |SMAX32 |1 |1
|49 |SMBB32 |2 |1
|50 |SMBT32 |2 |1
|51 |SMTT32 |2 |1
|52 |SMDS32 |3 |1
|53 |SMDRS32 |3 |1
|54 |SMXDS32 |3 |1
|55 |SMIN32 |1 |1
|56 |SRA32 |1 |1
|57 |SRA32.u |1 |1
|58 |SRAI32 |1 |1
|59 |SRAI32.u |1 |1
|60 |SRAIW.U |1 |1
|61 |SRL32 |1 |1
|62 |SRL32.u |1 |1
|63 |SRLI32 |1 |1
|64 |SRLI32.u |1 |1
|65 |STAS32 |1 |1
|66 |STSA32 |1 |1
|67 |SUB32 |1 |1
|68 |UKADD32 |1 |1
|69 |UKCRAS32 |1 |1
|70 |UKCRSA32 |1 |1
|71 |UKSTAS32 |1 |1
|72 |UKSTSA32 |1 |1
|73 |UKSUB32 |1 |1
|74 |UMAX32 |1 |1
|75 |UMIN32 |1 |1
|76 |URADD32 |1 |1
|77 |URCRAS32 |1 |1
|78 |URCRSA32 |1 |1
|79 |URSTAS32 |1 |1
|80 |URSTSA32 |1 |1
|81 |URSUB32 |1 |1"""

all_insn = []
for i,insn in enumerate(all_rv.split("\n")):
    n = insn.split("|")[2][:-1]
    print(i, n)
    all_insn.append(n.lower())

for i,insn in enumerate(all_rv64.split("\n")):
    n = insn.split("|")[2][:-1]
    print(i, n)
    all_insn.append(n.lower())


def pattern1(name, attr):
    return f"(?<=<<<[\n]+[\[#[\w]+\]\s+|\n]?===)\s+{name}\n+[\=|\w|\-| |/|\(|\)|\n|\&|\.|:|\*]+\s+\*{attr}:\*\s*([\w| |\(|\)]+)"




all_insn_k = {n:{'type':'None','extension':'None'} for n in all_insn}

# handle `type`
with open("./doc.txt","r") as f:
    txt = f.read()
    for n,typ in re.findall(r"(?<=<<<[\n]+[\[#[\w]+\]\s+|\n]?===)\s+([\w|\.]+)[\w|\-| |\(|\)|\&]+[\n]+\*Type:\*[\s]*([\w|\-| |\(|\)]+)",txt):
        if n.lower() not in all_insn:
            all_insn_k[n.lower()] = {'type':typ, "extension":"None"}
        else:
            all_insn_k[n.lower()]['type'] = typ


# handle `extension`
with open("./doc.txt","r") as f:
    txt = f.read()
    for n,typ in re.findall(r"(?<=<<<[\n]+[\[#[\w]+\]\s+|\n]?===)\s+([\w|\.]+)[\w|\-| |\(|\)|\&]+[\n]+\*Extension:\*[\s]*([\w|\-| |\(|\)]+)",txt):  
        if n.lower() not in all_insn:
            all_insn_k[n.lower()] = {'type':"None", "extension":typ}
        else:
            all_insn_k[n.lower()]['extension'] = typ

# handle `Sub-extension`
with open("./doc.txt","r") as f:
    txt = f.read()
    for n,typ,ext in re.findall(r"(?<=<<<[\n]+[\[#[\w]+\]\s+|\n]?===)\s+([\w|\.]+)[\w|\-| |\(|\)|\&]+[\n]+\*Type:\*[\s]*([\w|\-| |\(|\)]+)\n+\*Sub-extension:\*[\s]*([\w|\-| |\(|\)]+)",txt):  
        if n.lower() not in all_insn:
            all_insn_k[n.lower()] = {'type':"typ", "extension":ext}
        else:
            assert(all_insn_k[n.lower()]['extension'] == 'None')
            all_insn_k[n.lower()]['type'] = typ
            all_insn_k[n.lower()]['extension'] = ext

with open("./doc.txt","r") as f:
    txt = f.read()
    for n,typ,ext in re.findall(r"(?<=<<<[\n]+[\[#[\w]+\]\s+|\n]?===)\s+([\w|\.]+)[\w|\-| |\(|\)|\&]+[\n]+\*Type:\*[\s]*([\w|\-| |\(|\)]+)\n+[[[\w|\-| |\(|\)|\&|:|\.]+\n+]?\*Sub-extension:\*[\s]*([\w|\-| |\(|\)]+)",txt):  
        print(n,typ, ext)
        if n.lower() not in all_insn:
            all_insn_k[n.lower()] = {'type':"typ", "extension":ext}
        else:
            assert(all_insn_k[n.lower()]['extension'] == 'None')
            assert(all_insn_k[n.lower()]['type'] != 'None')
            all_insn_k[n.lower()]['type'] = typ
            all_insn_k[n.lower()]['extension'] = ext            

            
with open("./doc.txt","r") as f:
    txt = f.read()
    for m in re.findall(r"(?<=<<<[\n]+[\[#[\w]+\]\s+|\n]?===)\s+([\w|, |\.|]+)", txt):
        km = m.split(',')
        if len(km) >1:
            
            # type
            pp = pattern1(m, 'Type')
            a = re.findall(pp, txt)
            typ = 'None'
            extension = 'None'
            if len(a) == 1:
                a = a[0]
  
                typ = a
            else:
                print(f"error: unable to parse type:{m}")
            
            
            
            # extension:
            pp = pattern1(m, 'Extension')
            a = re.findall(pp, txt)
            if len(a) == 1:
                a = a[0]
                extension = a

            else:
                pass
                #print(f"error: unable to parse extension:{m}")
            
            if extension == 'None':
                # extension:
                pp = pattern1(m, 'Sub-extension')
                a = re.findall(pp, txt)
                if len(a) == 1:
                    a = a[0]
                    extension = a

                else:
                    pass
                    print(f"error: unable to parse sub-extension:{m}")
            
            for k_ in km:
                k = k_.strip()
                if k.lower() not in all_insn:
                    all_insn_k[k.lower()] = {'type':typ, "extension":extension}
                else:
                    all_insn_k[k.lower()]['type'] = typ
                    all_insn_k[k.lower()]['extension'] = extension

        
            
    
c = 0
for k,v in all_insn_k.items():
    if v['type'] == 'None':
        print(k, v)
        c+=1
print(c)


# check Zpsfoperand
rv_zpsfoperand = """|1  |&#10003; |&#10003; |SMAL 
|2  |&#10003; |         |ADD64 
|3  |&#10003; |&#10003; |RADD64 
|4  |&#10003; |&#10003; |URADD64 
|5  |&#10003; |&#10003; |KADD64 
|6  |&#10003; |&#10003; |UKADD64
|7  |&#10003; |         |SUB64 
|8  |&#10003; |&#10003; |RSUB64 
|9  |&#10003; |&#10003; |URSUB64 
|10 |&#10003; |&#10003; |KSUB64 
|11 |&#10003; |&#10003; |UKSUB64
|12 |&#10003; |&#10003; |SMAR64 
|13 |&#10003; |&#10003; |SMSR64 
|14 |&#10003; |&#10003; |UMAR64 
|15 |&#10003; |&#10003; |UMSR64 
|16 |&#10003; |&#10003; |KMAR64 
|17 |&#10003; |&#10003; |KMSR64
|18 |&#10003; |&#10003; |UKMAR64 
|19 |&#10003; |&#10003; |UKMSR64 
|20 |&#10003; |&#10003; |SMALBB 
|21 |&#10003; |&#10003; |SMALBT 
|22 |&#10003; |&#10003; |SMALTT
|23 |&#10003; |&#10003; |SMALDA 
|24 |&#10003; |&#10003; |SMALXDA 
|25 |&#10003; |&#10003; |SMALDS 
|26 |&#10003; |&#10003; |SMALDRS 
|27 |&#10003; |&#10003; |SMALXDS
|28 |&#10003; |&#10003; |SMSLDA 
|29 |&#10003; |&#10003; |SMSLXDA 
|30 |&#10003; |&#10003; |MULR64 
|31 |&#10003; |&#10003; |MULSR64
|32 |&#10003; |&#10003; |UMUL8 
|33 |&#10003; |&#10003; |UMULX8 
|34 |&#10003; |&#10003; |UMUL16 
|35 |&#10003; |&#10003; |UMULX16 
|36 |&#10003; |&#10003; |SMUL8 
|37 |&#10003; |&#10003; |SMULX8 
|38 |&#10003; |&#10003; |SMUL16 
|39 |&#10003; |&#10003; |SMULX16 
|40 |         |&#10003; |WEXTI"""

for n_ in rv_zpsfoperand.split("\n"):
    n = n_.split("|")[-1].lower().strip()
    if n not in all_insn_k:
        print(f"error: {n} is not parsed.")
    elif all_insn_k[n]['extension'] != 'Zpsfoperand':
        print(f"error: {n} ext is not valid.")

#check Zbpbo
rv_zbpbo = """| &#10003; |          |  CLZ         | Count leading zero
| &#10003; | &#10003; |  PACK        | Pack
| &#10003; | &#10003; |  PACKU       | Pack upper
| &#10003; |          |  FSR         | Funnel shift right
| &#10003; |          |  FSRI        | Funnel shift right immediate
|          | &#10003; |  FSRW        | Funnel shift right word
| &#10003; | &#10003; |  MAX         | Maximum
| &#10003; | &#10003; |  MIN         | Minimum
| &#10003; | &#10003; |  REV8.H      | Swap byte within halfword
| &#10003; | &#10003; |  CMIX        | Conditional bit selection
| &#10003; | &#10003; |  REV         | Bit reverse"""
for n_ in rv_zbpbo.split("\n"):
    n = n_.split("|")[3].lower().strip()
    if n not in all_insn_k:
        print(f"error: {n} is not parsed.")
    elif 'Zbpbo' not in all_insn_k[n]['extension']:
        print(f"error: {n} ext is not valid.")

        
#check rv64 only
for i,insn in enumerate(all_rv64.split("\n")):
    n = insn.split("|")[2][:-1].lower()
    if n in all_insn_k:
        if 'RV64 Only' not in all_insn_k[n]['type'] and 'RV64 only' not in all_insn_k[n]['type']:
            print(f"error: {n} must be rv64 only, but its type is {all_insn_k[n]['type']}")
        pass
    else:
        print(f"error:{n} not in table.")
        
        
all_typ = {}
for n,attr in all_insn_k.items():
    if  attr['type'] not in all_typ:
        all_typ[attr['type']] = 1
print(all_typ)

all_ext = {}
for n,attr in all_insn_k.items():
    if  attr['extension'] not in all_ext:
        all_ext[attr['extension']] = 1
    else:
        all_ext[attr['extension']] += 1
        
        
print(all_ext)


for n,attr in all_insn_k.items():
    if attr['extension'] == 'None':
        if  attr['type'] == 'RV32 Only':
            all_insn_k[n]['extension'] = 'zpn32'
        elif attr['type'] in  ['SIMD (RV64 Only)', 'SIMD (RV64 only)','DSP (RV64 Only)', 'DSP (RV64 only)'] :
            all_insn_k[n]['extension'] = 'zpn64'
        elif attr['type'] in ['SIMD', 'DSP','RV32 and RV64','Partial-SIMD','Partial-SIMD (Reduction)']:
            all_insn_k[n]['extension'] = 'zpn'
    else:
        if attr['extension'] in ['Zbpbo (RV32)', 'Zbpbo (RV32']:
            attr['extension'] = "zbpbo32"
        elif attr['extension'] in ['Zbpbo (RV64)']:
            attr['extension'] = "zbpbo64"
        elif attr['extension'] in ['Zbpbo (RV32 and RV64)']:
            attr['extension'] = "zbpbo"
        elif attr['extension'] in ['Zpsfoperand']:
            if  attr['type'] == 'RV32 Only':
                all_insn_k[n]['extension'] = 'zpsfoperand32'
            elif attr['type'] in  ['SIMD (RV64 Only)', 'SIMD (RV64 only)','DSP (RV64 Only)', 'DSP (RV64 only)'] :
                all_insn_k[n]['extension'] = 'zpsfoperand64'
            elif attr['type'] in ['SIMD', 'DSP','RV32 and RV64','Partial-SIMD','Partial-SIMD (Reduction)']:
                all_insn_k[n]['extension'] = 'zpsfoperand'

for n_,attri in all_insn_k.items():
    
    ress=[]
    
    dd = re.findall(r'([\D]+)i([\d]*[w]?[\.]?[u]?$)',n_)
    if len(dd) == 1:
        n = "".join(dd[0])
    else:
        n = n_
    original_n = n_
    if n.find('.')!=-1:
        original_n = original_n.replace('.','_')
        n = n.replace('.','_')
    
    pp = [f"([\w]+)\s+(__rv_)([u|s]?{n})\(([\w|,| ]+)\);\n*", f"([\w]+)\s+(__rv_v_)([u|s]?{n})\(([\w|,| ]+)\);\n*"]
    len_0 = 0
    for i,p in enumerate(pp):
        
        res = re.findall(p, txt)
        
        if len(res)>0:
            if i == 0:
                len_0 = len(res)
                
           
            if i == 0 and res[0][2] == n:
                if(len(res)!= 1):
                    assert(len(res) == 2)
                    if("".join(res[0]) == "".join(res[1])):
                        res = [res[0]]
                        len_0 = len(res)
                    else:
                        res = re.findall(f"([\w]+)\s+(__rv_)({n})\(([\w|,| ]+)\);\n*", txt)
                        len_0 = len(res)
                        assert(len(res) > 0)
            
            
                
                
            
            if i > 0 and res[0][2] == n:
                if len_0 == 1 and len(res) > 2:
                    res = re.findall(f"([\w]+)\s+(__rv_v_)({n})\(([\w|,| ]+)\);\n*", txt)
                    if len(res) == 2:
                        if("".join(res[0]) == "".join(res[1])):
                            res = [res[0]]
                
                assert(len(res) % len_0 == 0 or len(res) == 1)
                
                        
            if i == 0 and res[0][2] != n:
                assert(len(res) == 2)
            
            if all_insn_k[n_]['extension'] in ["zpsfoperand", "zpn", "zbpbo"]:
                tt = '*'
            elif '32' in all_insn_k[n_]['extension']:
                tt = '32'
            else:
                tt = '64'
                
           
            if len(res)== 1 and res[0][2] != n:
                print(f"error: {n} can not find intrinsics")
            else:
                nn = {}
                for ii, r_ in enumerate(res):
                    r = list(r_)
                    
                        
                    if tt == '*' and i > 0 and len(res) > 1:
                        if r[2] not in nn:
                            r.append("32")
                        else:
                            r.append("64")
                    else:
                        r.append(tt)
                        
                    if r[2] not in nn:
                        nn[r[2]] = 1
                    
                    ress.append(r)
    if len(ress) == 0:
        print(f"error: {n} can not find intrinsics")
    else:
        
        start = " +"
        other = "[\w| |#|,]+"
        the_len = -1
        imm_idx = -1
        if n_.endswith(".u"):
            assert(len(n_.split(".")) == 2)
            d = n_.split(".")[0].upper() + ".u"

            p = f"{start}{d}\s+(Rd,{other})"
        elif n_ in ['kdmbb', 'kdmbt', 'kdmtt']:
            p = f"{start}KDMxy\s+(Rd,{other})"
        elif n_ in ['kdmabb', 'kdmabt', 'kdmatt']:
            p = f"{start}KDMAxy\s+(Rd,{other})"
        elif n_ in ['khmbb', 'khmbt', 'khmtt']:
            p = f"{start}KHMxy\s+(Rd,{other})"
        elif n_ in ['sunpkd810', 'sunpkd820', 'sunpkd830', 'sunpkd831', 'sunpkd832']:
            p = f"{start}SUNPKD8xy\s+(Rd,{other})"
        elif n_ in ['zunpkd810', 'zunpkd820', 'zunpkd830', 'zunpkd831', 'zunpkd832']:
            p = f"{start}ZUNPKD8xy\s+(Rd,{other})"
        elif n_ in ['kdmbb16', 'kdmbt16', 'kdmtt16']:
            p = f"{start}KDMxy16\s+(Rd,{other})"
        elif n_ in ['kdmabb16', 'kdmabt16', 'kdmatt16']:
            p = f"{start}KDMAxy16\s+(Rd,{other})"
        elif n_ in ['khmbb16', 'khmbt16', 'khmtt16']:
            p = f"{start}KHMxy16\s+(Rd,{other})"
        elif n_ == 'urstsa16':
            p = f"{start}URCRSA16\s+(Rd,{other})"
        else:
            p = f"{n_.upper()}\s+(Rd,{other})"
        p_out = re.findall(p, txt)
        if len(p_out) == 0:
            print(n_)
        else:
            if n_ == 'rev':
                p_out = [p_out[0]]
            
            
            for o in p_out:
                
                zs = [d.strip() for d in o.split(",")]
                assert(len(zs) > 0)
                if the_len == -1:
                    the_len = len(zs)
                else:
                    assert(the_len == len(zs))
                for i,z in enumerate(zs):
                    if 'imm' in z:

                        if imm_idx == -1:
                            imm_idx = i
                        else:
                            assert(imm_idx == i)

        
        eles = []
        for res in ress:
            output_typ = res[0].strip()
            name = "".join(res[1:3])
            input_str = res[3]
            if len(input_str.split(",")) > 1:
                inputs = [d.lstrip().split(" ")[0] for d in input_str.split(",")]
            else:
                inputs = [input_str.split(" ")[0]]
            out_reg_typ = 'N'
            input_reg_typ = ['N' for _ in range(len(inputs))]
            if the_len != -1 and imm_idx != -1:
                
                if n_ in ['insb']:
                    assert(len(inputs) == the_len)
                    if imm_idx != -1:
                        input_reg_typ[imm_idx] = 'Y'
                else:
                   
                    assert(len(inputs) + 1  == the_len)
                    if imm_idx != -1:
                        input_reg_typ[imm_idx - 1] = 'Y'
                
            ele = {"types":[output_typ,*inputs],"n_operand":the_len, "is_imm":[out_reg_typ, *input_reg_typ], "name":name,"xlen":res[-1]}
            eles.append(ele)
        
        all_insn_k[n_]["intrinsics"] =      eles
        
        
        

dump = []
for k,ele in all_insn_k.items():
    dump.append({"insn":k,**ele})


with open("a.json","w") as f:
    f.write(json.dumps({"insns":dump},indent=2, sort_keys="insn"))
