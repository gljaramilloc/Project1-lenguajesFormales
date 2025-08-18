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

 - 1. From your computer, clone my repository with all the files included (dfa_minimizer.py, input.txt, and the README.md file).

 - 2. After cloning, open the terminal and run the command:
python dfa_minimizer.py
(Preferably do this from Visual Studio Code). This will display the result of the program execution.

 - 3. The file input.txt is the program’s input. I have already included a test case that will work when you run it.
However, if you want to test the program with another example, follow these instructions to provide a new input:

### DFA Specification

#### Alphabet Symbols
c n alphabet_symbols

#### Final States
final_states

#### Transition Row 0
transition_row_0

#### Transition Row 1
transition_row_1

#### Transition Row 2
transition_row_2

#### Transition Row n-1
transition_row_n-1

where: 
- `c`: number of test cases (DFAs).  
- `n`: number of states in the DFA.  
- `alphabet_symbols`: alphabet symbols separated by spaces.  
- `final_states`: final states separated by spaces.  
- Each transition row corresponds to one state and contains the destination states in the same order as the alphabet symbols.

# DFA Minimization - Code Explanation

This project implements a DFA (Deterministic Finite Automaton) minimization algorithm in Python.  
The core function is `minimize_dfa`, which finds **equivalent states** using the **table-filling method**.

---

## 📌 Function: `minimize_dfa(n, alphabet, finals, delta)`

### Parameters
- **n** → Number of states in the DFA.  
- **alphabet** → List of alphabet symbols.  
- **finals** → Set of final (accepting) states.  
- **delta** → Transition table, represented as a 2D list where:
  - Each row corresponds to a state.  
  - Each column corresponds to the destination state under a given input symbol.

---

### 🔎 Step by Step Explanation

#### **Step 1: Initialize the table of pairs**
```python
marked = [[False] * n for _ in range(n)]

-A 2D table marked is created.
Each entry (p, q) indicates whether states p and q are distinguishable.

Initially, all pairs are set to False (not marked as different).

Step 2: Mark pairs where one state is final and the other is not
for p in range(n):
    for q in range(p + 1, n):
        if (p in finals) != (q in finals):
            marked[p][q] = True


If one state is accepting and the other is not, they cannot be equivalent.

Such pairs (p, q) are marked as distinguishable immediately.

Step 3: Iteratively mark distinguishable pairs
changed = True
while changed:
    changed = False
    for p in range(n):
        for q in range(p + 1, n):
            if not marked[p][q]:
                for sym in range(len(alphabet)):
                    p_next = delta[p][sym]
                    q_next = delta[q][sym]
                    x, y = sorted((p_next, q_next))
                    if marked[x][y]:
                        marked[p][q] = True
                        changed = True
                        break


This is the core of the table-filling algorithm.

For each pair (p, q) not yet marked:

Look at their transitions for each input symbol.

If their next states (p_next, q_next) are already distinguishable, then (p, q) must also be distinguishable.

This process repeats until no new pairs are marked.

Step 4: Collect equivalent pairs
result = []
for p in range(n):
    for q in range(p + 1, n):
        if not marked[p][q]:
            result.append(f"({p},{q})")


After the iterations, any pair (p, q) not marked as distinguishable is equivalent.

These pairs are returned in a list.

📌 Function: main()

The main function handles reading the input and executing the minimization.

Read input from input.txt.

First line → number of test cases.

Next → states, alphabet, final states, and transition table.

Call minimize_dfa for each case.

Print equivalent pairs separated by spaces.
