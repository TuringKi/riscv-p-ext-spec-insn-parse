You don't need to regenerate the JSON again. The `insn.json` file in the repository has been manually checked and verified.

Steps
```bash
# download the spec
wget https://raw.githubusercontent.com/riscv/riscv-p-spec/master/P-ext-proposal.adoc -o doc.txt

#generate the draft json (just for demo, no need to do it)
python3 ./gen_insn_json_draft.py

#do some manual correction


#generate test-suites
python3 ./gen_testsuites.py

```