class Solution(object): #runtime is 16ms
    def interpret(self, command):
        newStr = command.replace('()','o').replace('(al)','al')
        #if we dont use replace, what we can try is finding whenever '(' occurs,
        #from there, we determine what text is there before the ')', this would definitely 
        #tank the runtime and memory tho as it would require a loop
        
        return(newStr)

#runtime is 20ms so virtually no difference
class Solution(object):
    def interpret(self, command):
        newStr= ''
        i = 0
        while i < len(command):
            if command[i] == "G":
                newStr+= 'G'
            elif command[i] == "(" and command[i+1] == ')':
                newStr+= 'o'
            elif command[i] == "(" and command[i+1] == "a":
                newStr+="al"
            i+=1
        return(newStr)