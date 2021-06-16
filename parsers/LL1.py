import pandas as pd
import numpy as np
import sys

#pr={'S!':['S'],'S':['AA'],'A':['aA','b']}

def generatell1(pr2,inp):
    pr3=""
    for i in pr2:
        if(i!=' '):
            pr3+=i
    print(pr3)
    pr={}

    for i in pr3.split('\n'):
        j = i.split('->')
        q=j[1].split(',')
        pr[j[0]]=q

    #pr={'S!':['S'],'S':['ABC'],'A':['a','#'],'B':['b','#'],'C':['c','#']}
    print(pr)

    NT=list(pr.keys())

    T=[]
    for i in pr:
        for j in pr[i]:
            for z in j:
                if ((z.islower()) and (z not in T)):
                    T.append(z)


    print("Production Rules :",pr)
    print("Non-Terminals :",NT)
    print("Terminals :",T)

    pr1=[]

    for j in list(pr.keys()):
        for z in pr[j]:
            pr1.append([j,z])

    q1={}
    q2={}

    def qq1(a):
        if(a[0] in T):
            return a[0]
        b=[]
        if(len(a)==1):
            if(a=='#'):
                return['#']

        for i in pr[a[0]]:
            cc=qq1(i)
            for j in cc:
                if j not in b:
                    b.append(j)
        if(len(a)>1):
            if '#' in b:
                b.remove('#')
                cc=qq1(a[1:])
                for j in cc:
                    if j not in b:
                        b.append(j)
        return b


    qqq1=[]



    def qq2(a):
        qqq1.append(a)
        b=[]
        for i in NT:
            for j in pr[i]:
                if(j=='#'):
                    continue
                for zz in range(0,len(j)):
                    if (j[zz]==a and zz<len(j)-1):
                        cc=qq1(j[zz+1:])
                        for z in cc:
                            if z not in b:
                                b.append(z)
                    elif (j[zz]==a and zz==len(j)-1):
                        if(i=='S!'):
                            b.append('$')
                            continue
                        if i not in qqq1:
                            cc=qq2(i)
                            for z in cc:
                                if z not in b:
                                    b.append(z)
        return b


    def qqq2(a):
        qqq1.clear()
        z=qq2(a)
        if '#' in z:
            z[z.index('#')]='$'
        return z

    for i in NT[1:]:
        q1[i]=qq1(i)
        q2[i]=qqq2(i)

    qqqq1={}
    qqqq2={}

    qqqq1['S!']=[]
    for i in q1['S']:
        qqqq1['S!'].append(i)
    
    qqqq2['S!']=['$']

    for i in q1:
        qqqq1[i]=q1[i]
    for i in q2:
        qqqq2[i]=q2[i]
    q1=qqqq1
    q2=qqqq2

    print("First :",q1)
    print("Follow :",q2)

    q=[]
    for i in T:
        q.append(i)

    q.append('$')

    tab=pd.DataFrame(index=NT,columns=q)

    tab=tab.fillna("")

    c=[]

    for i in NT:
        for j in q1[i]:
            for z in pr[i]:
                if j in qq1(z):
                    if(j=='#'):
                        j='$' 
                    if(tab.loc[i][j]==""):
                        tab.at[i,j]=i+" -> "+z
                        continue
                    c.append([i,j])
                    tab.at[i,j]=tab.loc[i][j]+" , "+i+" -> "+z

    print(tab)         

    s="<div class=\"titlespace\"><h1 id=\"title1\">LL(1)</h1></div><div id=\"outbox1\"><div id=\"firstfollow\"><div class=\"absline\"></div><div class=\"titles\"><div class=\"ftitle2\"><h4 class=\"ftitle1\">FIRST</h2></div><div class=\"ftitle2\"><h4 class=\"ftitle1\">FOLLOW</h2></div></div><div class=\"lists\"><ul class=\"list\">"
    
    for i in list(q1.keys()):
        s+="<li>"+i+" : "+q1[i][0]
        for j in q1[i][1:]:
            s+=","+j
        s+="</li>"
    s+="</ul><ul class=\"list\">"

    for i in list(q2.keys()):
        s+="<li>"+i+" : "+q2[i][0]
        for j in q2[i][1:]:
            s+=","+j
        s+="</li>"
    s+="</ul></div></div>"

    s+="<table id=\"table1\"><caption>LL(1) Table</caption><tr><th id=\"table1h1\"></th>"
    for i in T:
        s+="<th>"+i+"</th>"
    s+="<th id=\"table1h2\">$</th>"

    s+="</tr>"
    qqqqq=list(tab.index)
    for i in qqqqq[:-1]:
        s+="<tr><th>"+i+"</th>"
        for j in list(tab.loc[i]):
            s+="<td>"+j+"</td>"
        s+="</tr>"
    s+="<tr><th id=\"table1h3\">"+qqqqq[-1]+"</th>"
    for j in list(tab.loc[qqqqq[-1]][:-1]):
        s+="<td>"+j+"</td>"
    s+="<td id=\"table1h4\">"+tab.loc[qqqqq[-1]][-1]+"</td>"
    s+="</tr></table>"


    print("Conflicts : ",c)
    s+="<div id=\"conflicts\"><h3>Conflicts</h3><ul>"
    if(len(c)>0):
        print("Conflicts Exist")
        print("The Grammer is not an LL(1) grammer")

        for i in c:
            s+="<li>"+i[0]+"->"+i[1]+"</li>"
        s+="</ul></div>"
        return s
    
    s+="<li>No Conflicts Exists</li>"
    s+="</ul></div>"

    if(len(inp)==0):
        s+="</div>"
        print(s)
        return s


    st=[]
    st.append(NT[0])


    tabinp = pd.DataFrame(columns=['Stack','Input','Production'])


    i=0 
    zq=0
    while(i<len(inp)):
        q=inp[i]
        if((len(st)==0) or (q not in T)):
            zq=1
            break
        if(st[-1] in T):
            if(st[-1]==inp[i]):
                i+=1
                st.pop()
                continue
        if(st[-1] in NT):
            if(tab.loc[st[-1]][q]==""):
                if(tab.loc[st[-1]]['$']!=""):
                    qq=st[-1]
                    qqq=""
                    st.reverse()
                    for j in st:
                        qqq+=j
                    st.reverse()
                    st.pop()
                    row={'Stack':qqq+'$','Input':inp[i:],'Production':tab.loc[qq]['$']}
                    tabinp = tabinp.append(row,ignore_index=True)
                    continue
                zq=1
                break
            qq=st[-1]
            qqq=""
            st.reverse()
            for j in st:
                qqq+=j
            st.reverse()
            st.pop()
            if(tab.loc[qq][q][-1]!='#'):
                for j in range(len(tab.loc[qq][q])-1,tab.loc[qq][q].index('>')+1,-1):
                    st.append(tab.loc[qq][q][j])
            row={'Stack':qqq+'$','Input':inp[i:],'Production':tab.loc[qq][q]}
            tabinp = tabinp.append(row,ignore_index=True)
            continue
        break

    qqq=""
    st.reverse()
    for j in st:
        qqq+=j
    st.reverse()

    row={'Stack':qqq+'$','Input':"",'Production':""}
    tabinp = tabinp.append(row,ignore_index=True)

    print(tabinp)

    s+="<div id=\"parsing\"><table id=\"table1\" id=\"table\"><caption>Parsing the Input String</caption>"
    s+="<tr><th id=\"table1h1\"></th><th>Stack</th><th>Input</th><th id=\"table1h2\">Production</th></tr>"
    
    qqqqq=list(tabinp.index)
    for i in qqqqq[:-1]:
        s+="<tr><th>"+str(i)+"</th>"
        for j in list(tabinp.loc[i]):
            s+="<td>"+j+"</td>"
        s+="</tr>"
    s+="<tr><th id=\"table1h3\">"+str(qqqqq[-1])+"</th>"
    for j in list(tabinp.loc[qqqqq[-1]][:-1]):
        s+="<td>"+j+"</td>"
    s+="<td id=\"table1h4\">"+tabinp.loc[qqqqq[-1]][-1]+"</td>"
    s+="</tr></table>"

    if(zq):
        s+="<li id=\"parseresult\">The Input String is Not Accepted by the Grammar</li></div></div>"
        print("The Input String is Not Accepted by the Grammer")
        return s
    if(len(st)==0):
        s+="<li id=\"parseresult\">The Input String is Accepted by the Grammar</li></div></div>"
        print("The Input String is Accepted by the Grammer")
        return s
    s+="<li id=\"parseresult\">The Input String is Not Accepted by the Grammar</li></div></div>"
    print("The Input String is Not Accepted by the Grammer")
    print(s)
    return s

