# DFA Minimization Project

## 📌 Student Information
- **Full Name:** [Gisel Lorena Jaramillo]  
- **Class Number:** [C2566-SI2002-5464]  

---

## 🖥️ Environment and Tools
- **Operating System:** Windows 10 / 11 (64-bit)  
- **Programming Language:** Python 3.12  
- **Editor/Tools Used:** Visual Studio Code / PowerShell / CMD  

---

## 🚀 Running Instructions

1. **Clone or copy** the project files into a folder.  
   Make sure the following files exist:
   - `dfa_minimizer.py` (your implementation)
   - `input.txt` (the input file with DFA definitions)

2. **Prepare the input file** (`input.txt`) using the following format:
c
n
alphabet_symbols
final_states
transition_row_0
transition_row_1
...
transition_row_n-1

- `c`: number of test cases (DFAs).  
- `n`: number of states in the DFA.  
- `alphabet_symbols`: alphabet symbols separated by spaces.  
- `final_states`: final states separated by spaces.  
- Each transition row corresponds to one state and contains the destination states in the same order as the alphabet symbols.

3. **Run the program** with:
```bash
python dfa_minimizer.py