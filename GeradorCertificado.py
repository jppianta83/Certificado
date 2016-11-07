s = ""
l=[]
f = open('saida.txt', 'w')
while(s!="pronto"):
    s = input()
    if s == "remover":
        del l[len(l)-1]
        print(l)
    else:
        if s!="pronto":
            l.append(s.upper())
            print(l)
s = input()
s1 = input()
s2 = input()

f.write("\\documentclass{beamer}\n\\usepackage[usenames, dvipsnames]{color}\n\\usepackage[utf8]{inputenc}\n\\definecolor{mybrown}{rgb}{0.20, 0.08, 0.08}\n")
f.write("\\usebackgroundtemplate%\n{%\n\\includegraphics[width=\\paperwidth,height=\\paperheight]{tem.png}%\n}\n\\usetheme{default}\n\\AtBeginSubsection[]\n")
f.write("{\n\\begin{frame}<beamer>{Outline}\n\\tableofcontents[currentsection,currentsubsection]\n\\end{frame}\n}\n\\beamertemplatenavigationsymbolsempty\n\\begin{document}\n")

for st in l:
    f.write("\\begin{frame}[c]\n")
    f.write("\\centerline{\\textbf{\\Huge{\\color{mybrown}{Certificado}}}}\n")    
    f.write("\\vspace{10 mm}\n")      
    f.write("\\centerline{Certificamos que "+st+"}\n")      
    f.write("\\centerline{participou do treinamento}\n")
    f.write("\\centerline{“"+s+"”,}\n")           
    f.write("\\centerline{com duração de "+s1+" horas, realizado nos dias}\n")
    f.write("\\centerline{"+s2+"}\n")         
    f.write("\\vspace{6.6 mm}\n")
    f.write("\\centerline{\\includegraphics[scale=0.2]{assin.png}}")
    f.write("\\vspace{-6 mm}")
    f.write("\\centerline{\\underline{\\hspace{2.8in}}}\n")      
    f.write("\\vspace{2 mm}\n")      
    f.write("\\centerline{Denise Kapper Ramos}\n")      
    f.write("\\end{frame}\n\n\n")

f.write("\\end{document}")
