import re  

def arithmetic_arranger(problems,solve=False):

 
  if len(problems)>5:
    return "Error: Too many problems."

  top_line=""
  bottom_line=""
  dash_line=""
  solution_line=""
  
  arranged_line="" 

  for problem in problems:
    new_list=problem.split()
    numerator=new_list[0]
    operator=new_list[1]
    denominator=new_list[2]
    
    if operator=="*" or operator=="/":
      return "Error: Operator must be '+' or '-'."

    if re.search("[^\d]",numerator) or re.search("[^\d\+\-]",denominator):
      return "Error: Numbers must only contain digits."

    if len(numerator)>4 or len(denominator)>4:
      return "Error: Numbers cannot be more than four digits."
    
    answer=""
    if operator=="+":
      answer=str(int(numerator)+ int(denominator))
    elif operator == "-":
      answer=str(int(numerator) - int(denominator))
  

    line_length=max(len(numerator),len(denominator))+2
   
    numerator_line=""
    numerator_line = str(numerator.rjust(line_length))
    
    denominator_line=""
    denominator_line =str(operator) + str(denominator.rjust(line_length - 1))
    
    dash=""
    for p in range(line_length):
      dash +="-"
    

    
    answer_line=""
    answer_line += answer.rjust(line_length)
  
    if problem != problems[-1]:
      top_line += numerator_line + "    "
      bottom_line += denominator_line + "    "
      dash_line += dash + "    "
      solution_line += answer_line + "    "
    else:
      top_line += numerator_line 
      bottom_line += denominator_line 
      dash_line += dash 
      solution_line += answer_line

  if solve==True:
    arranged_line = top_line + "\n" + bottom_line + "\n" + dash_line + "\n" + solution_line
  else:
    arranged_line = top_line + "\n" + bottom_line + "\n" + dash_line



   
  return arranged_line