"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    len1=len(line1)
    len2=len(line2)
    if len1<=len2:
        short_len=len1
    else:
        short_len=len2
    if short_len==0:
        if len1==len2:    
            return IDENTICAL
        else:
            return 0
    for idx in range(0,short_len):
        if line1[idx]!=line2[idx]:
            break
    result=idx
    #check substring
    if line1[idx]==line2[idx]:
        if len1==len2:
            return IDENTICAL
        else:
            result=short_len
    return result

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if '\n'in line1 or '\r'in line1:
        return ""
    if '\n'in line2 or '\r'in line2:
        return ""
    if idx<0:
        return ""
    if idx>0:
        if idx>len(line1) or idx>len(line2):
            return ""
    middle=''
    if idx>0:
        count=idx-1
        while count>=0:
            middle+='='
            count-=1
    middle+='^'
    result=line1+'\n'+middle+'\n'+line2+'\n'
    return result

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    len1=len(lines1)
    len2=len(lines2)
    if len1<=len2:
        short_len=len1
    else:
        short_len=len2
    if short_len==0:
        if len1==len2:    
            return (IDENTICAL,IDENTICAL)
        else:
            return (0,0)
    str_idx=0
    for str_idx in range(short_len):
        ch_idx=singleline_diff(lines1[str_idx], lines2[str_idx])
        if ch_idx!=IDENTICAL:
            break
    result=(str_idx,ch_idx)
    if (str_idx==short_len-1) and (ch_idx==IDENTICAL):
        if len1==len2:
            return (IDENTICAL, IDENTICAL)
        else:
            result=(short_len,0)
    return result

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    result=[]
    with open(filename,'rt',encoding="utf8") as file_obj:
        for line in file_obj:
            new_line=list(line)
            if new_line[-1]=='\n' or new_line[-1]=='\r':
                new_line.pop(-1)
            if len(new_line)>0:
                string=''.join(new_line)
            else:
                string=''
            result.append(string)
        file_obj.close()
        return result

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1=get_file_lines(filename1)
    lines2=get_file_lines(filename2)
    len1=len(lines1)
    len2=len(lines2)
    (str_idx,ch_idx)=multiline_diff(lines1,lines2)
    if (str_idx,ch_idx)==(IDENTICAL,IDENTICAL):
        result='No differences\n'
    else:
        result='Line '+str(str_idx)+':\n'
        if len1==0 and len2!=0:
            line2=lines2[str_idx]
            result+=singleline_diff_format('', line2, ch_idx)
        elif len1!=0 and len2==0:
            line1=lines1[str_idx]
            result+=singleline_diff_format(line1, '', ch_idx)
        elif len1==0 and len2==0:
            result+=singleline_diff_format('', '', ch_idx)
        else:
            line1=lines1[str_idx]
            line2=lines2[str_idx]
            result+=singleline_diff_format(line1, line2, ch_idx)

    return result
    
