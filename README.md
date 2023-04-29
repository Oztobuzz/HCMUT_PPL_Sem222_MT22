# HCMUT_PPL_Sem222_MT22
MT22 is a C-like language. It is similar enough to C to feel familiar, but different enough to give you some sense of alternatives.

## About the Project
This is my Principle of Programming Language's assignment. In this assignment, I was asked to build a C-like programming language (MT22) from scratch. The assignment is divided into 4 phases:

1. **Lexer and Parser:** Teach your language how to identify tokens and lexemes
   - _Input_: program. 
   - _Output_: Parse tree
   - _File modified_: [src/main/mt22/parser/MT22.g4](src/main/mt22/parser/MT22.g4)
2. **AST generation:** Build AST tree from Parse tree (omit some non-relevant symbols in parse tree)
   - _Input_: Parse tree
   - _Output_: AST tree
   - _File modified_: [src/main/mt22/astgen/ASTGeneration.py](src/main/mt22/astgen/ASTGeneration.py)
3. **Checker:** Doing static check and throw error when needed
   - _Input_: AST tree
   - _Output_: None if program have no errors in static check else throw errors
   - _File modified_: [src/main/mt22/checker/StaticChecker.py](src/main/mt22/checker/StaticChecker.py)
4. **Code Generation:** Run and generate code (values, results) from AST tree (Not yet)
   - _Input_: AST tree
   - _Output_: N/A
   - _File modified_: N/A

This repository includes **phase 1 to phase 3**.
### Built with
* <a href= "https://www.antlr.org/"><img src= "https://tomassetti.me/wp-content/uploads/2016/02/antlr-logo.png" width="200"  />
* <a href= "https://www.python.org/"><img src= "https://miro.medium.com/v2/resize:fit:1400/1*m0H6-tUbW6grMlezlb52yw.png" width="200"  />

## Getting Started

This is an instruction of how to run this language on your local machine. In order to be able to use run antlr files, you need to do there things
### Prerequisites:
* Java 19.0.2
* Python 3.11.2 (Current newest version)
* Antlr 4.9.2 
  
### Usage
After have installed all the necessary stuffs. Do following description in [Specification_Instruction/README.txt](Specification_Instruction/README.txt)
  
Set **environment variable ANTLR_JAR** to the file **antlr-4.9.2-complete.jar** in your computer
  
Change current directory to **initial/src** where there is file run.py
  
  Type:
  ```sh
  python run.py gen
  ```
  
  You can then type (omit the part in parentheses):
  ``` sh
  python run.py test LexerSuite (test your Lexer code)
  ```
  ``` sh
  python run.py test ParserSuite (test your Parser code)
  ```
  ```sh
  python run.py test ASTGenSuite (test your AST Gen code)
  ```
  ```sh
  python run.py test CheckerSuite (test your Static Checker code)
  ```
  ```sh
  python run.py test CodeGenSuite (test your Code Gen code)
  ```
These commands will run test files I have already built in [HCMUT_PPL_Sem222_MT22/src/test/](HCMUT_PPL_Sem222_MT22/src/test/). 
  
The **testcases** will then be exported to files in **folder testcases** while the **solutions** your code gives back will be exported to **folder solutions**. In order to make your own testcase, you just need to modify one of .py files in test folder.
  
  In every test files, I have already included 100 testcases each. Feel free to use to test your system _(No 100% guarantee though)_
 
  ### Make your own testcase
  One example of how to test your code using [src/test/CheckerSuiteone.py](src/test/CheckerSuiteone.py). This will do ** 1 testcase** for your system, you just need to modify **2 parts** in this file:
  1. _Input:_ your AST tree or source functions (Checker will receive both formats) 
  2. _Expect:_ None or the error your static checker will throw out (your expected result)

  Type  
  ```sh
  python run.py test CheckerSuiteone 
  ```
  in your cmd to run the testcase.
  
## License
Distributed under the GNU License. See `LICENSE.txt` for more information.
 
## Contact

Oanh Tran - oanh.tranotsc1123@hcmut.edu.vn

Project Link: [https://github.com/Oztobuzz/HCMUT_PPL_Sem222_MT22.git](https://github.com/Oztobuzz/HCMUT_PPL_Sem222_MT22.git) 

