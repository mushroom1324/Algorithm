form = input()
fixedForm = ''
index = 0
bracket = 0
const = 0

while len(form) > 0:
    if form[0] == '-':
        const = 0

        if bracket == 0:
            bracket = 1
            fixedForm += '-('
            form = form[1:]

        else:
            fixedForm += ')-('
            form = form[1:]

    else:
        if const == 0 and form[0] == '0':
            form = form[1:]
            continue

        if '1' <= form[0] <= '9':
            const = 1
        elif form[0] == '+':
            const = 0

        fixedForm += form[0]
        form = form[1:]
if bracket == 1 and fixedForm[len(fixedForm)-1] != ')':
    fixedForm += ')'

print(fixedForm)
print(eval(fixedForm))
