import pandas as pd
import numpy as np
import sys


def generateclr1(pr2,inp):
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
        return qq2(a)


    sta=[]
    st1={}
    q=NT[0]
    st1[q]=pr[q]
    st=[]
    trz={}
    stz=[]
    zz={}
    zzz={}
    for i in range(0,len(st1[q])):
        if (len(st1[q][i])>1):
            if(st1[q][i][0:2]==NT[0]):
                stz.append(NT[0])
        elif st1[q][i][0].isupper():
            stz.append([st1[q][i][0],['$']])
        z='.'+st1[q][i]
        z=[z,['$']]
        st1[q][i]=z

    trz={}
    trz[0]=[]


    while(len(stz)>0):
        q3=stz.pop()
        q=q3[0]
        if q not in st1.keys():
            st1[q]=pr[q]
            for j in range(0,len(st1[q])):
                if st1[q][j][0].isupper():
                    if(len(st1[q][j])==1):
                        z=q3[0]
                    else:
                        z=qq1(st1[q][j][1:])
                    stz.append([st1[q][j][0],z])
                trz[0].append(st1[q][j][0])
                st1[q][j]=['.'+st1[q][j],q3[1]]
    stn=2

    stnz=[]
    stnz.append(0)
    sta.append(st1)
    #print(sta)
    #print(trz)
    st.append(0)
    #zz[0]=[]

    st4={NT[0]:[NT[1]+'.',['$']]}
    sta.append(st4)
    zz[0]={}
    zz[0][NT[1]]=1

    while(len(st)>0):
        zx=st.pop()
        st2=sta[zx]
        stz=[]
        for i in trz[zx]:
            st3={}
            trz[stn]=[]
            zq=[]
            for j in st2.keys():
                for q3 in st2[j]:
                    z=q3[0]
                    x=z.index('.')
                    if(x<len(z)-1):
                        if ( z[x+1] == i ):
                            if j not in st3.keys():
                                st3[j]=[]
                            st3[j].append([z[:x]+z[x+1]+'.'+z[x+2:],q3[1]])
                            if ( x+2 < len(z)):
                                if(z[x+2] in NT):
                                    if (len(z)==x+3):
                                        q4=q3[1]
                                    else:
                                        q4=qq1(z[x+3:])
                                    stz.append([z[x+2],q4])
                                if ( z[x+2] not in trz[stn] ):
                                    trz[stn].append(z[x+2])
                                continue
                            if(j=='S!'):
                                zq.append(['accept'])
                                continue
                            qqqq=1
                            for qz in list(pr.keys())[1:]:
                                for zqq in pr[qz]:
                                    for q5 in range (0,len(st3[j])):
                                        if(zqq[0][1:]==st3[j][q5][0][:-1]):
                                            zq.append([qqqq,st3[j][q5][1]])
                                    qqqq+=1
                            continue



            xz={}
            for q3 in stz:
                j=q3[0]
                xz[j]=[]
                for z in pr[j]:
                    xz[j].append([z[0],q3[1]])
                    if(z[0][1] in NT ):
                        if(len(z[0])==2):
                            q4=q3[1]
                        else:
                            q4=qq1(z[0][2:])
                        stz.append([z[0][1],q4])
                    if(z[0][1] not in trz[stn]):
                        trz[stn].append(z[0][1])

            while(len(stz)>0):
                q3=stz.pop()
                q=q3[0]
                if q not in xz.keys():
                    xz[q]=pr[q]
                    for j in range(0,len(xz[q])):
                        if xz[q][j][0].isupper():
                            if(len(xz[q][j])==1):
                                z=q3[1]
                            else:
                                z=qq1(xz[q][j][1:])
                            stz.append([xz[q][j][0],z])
                        if(xz[q][j][0] not in trz[stn]):
                            trz[stn].append(xz[q][j][0])
                        xz[q][j]=['.'+xz[q][j],q3[1]]
        
            for j in list(xz.keys()):
                if j in list(st3.keys()):
                    for z in xz[j]:
                        st3[j].append(z)
                    continue
                st3[j]=xz[j] 

            qqq=0

            for qq in range( 0 , len(sta) ):
                if(sta[qq]==st3):
                    if(zx not in zz.keys()):
                        zz[zx]={}
                    zz[zx][i]=qq
                    qqq=1
                    break

            if(qqq==1):
                continue

            sta.append(st3)
            st.append(stn)
            if(len(zq)!=0):
                zzz[stn]=zq
            if(zx not in zz.keys()):
                zz[zx]={}
            zz[zx][i]=stn
            stn+=1
            continue

        

    print("States :")
    j=0
    for i in sta:
        print(j,":",i)
        j+=1

    qqq=sorted(zz.keys())
    print("Transitions : {",end="")
    for i in qqq:
        print(str(i),":",str(zz[i]),end="")
        if(i!=len(qqq)-1):
            print(" ,",end=" ")
    print("}")
    print("Reductions :",zzz)


    tdf={}

    for i in T:
        tdf[i]={}
        for j in range(0,len(sta)):
            tdf[i][j]=[-1,[]]
    for i  in NT:
        tdf[i]={}
        for j in range(0,len(sta)):
            tdf[i][j]=[-1,[]]
    tdf['$']={}
    for j in range(0,len(sta)):
        tdf['$'][j]=[-1,[]]
    for i in list(zz.keys()):
        for j in list(zz[i].keys()):
            tdf[j][i][0]=zz[i][j]
    for i in list(zzz.keys()):
        for z in T:
            for j in zzz[i]:
                tdf[z][i][1].append(j)
        for z in NT:
            for j in zzz[i]:
                tdf[z][i][1].append(j)

    for i in list(zzz.keys()):
        for j in zzz[i]:
            tdf['$'][i][1].append(j)

    print(tdf)

    c=len(NT)+len(T)
    zqqq=[]
    for i in T:
        zqqq.append(i)
    for i in NT:
        if(i!='S!'):
            zqqq.append(i)
            continue
        zqqq.append('$')

    tab=pd.DataFrame(index=np.arange(len(sta)),columns=zqqq)

    sc={}
    rc=[]


    for i in list(tdf.keys()):
        for j in list(tdf[i].keys()):
            if(tdf[i][j][0]!=-1):
                x='S'+str(tdf[i][j][0])
            else:
                x=""
            if ( (i in T) or ( i=='$') ) :
                for z in tdf[i][j][1]:
                    if( i in z[1] ):
                        if(len(x)==0):
                            x+='R'+str(z[0])
                            continue
                        x+=',R'+str(z[0])
            if('R' in x) and ('S' in x):
                sc[j]={}
                sc[j]['S']=x.count('S')
                sc[j]['R']=x.count('R')
            if(x.count('R')>1):
                rc[j]=x.count('R')

            tab.iloc[j][i]=x 

    tab.iloc[1]['$']='accept'
    tdf['$'][1][0]=-2

    print(tab)
    print("SR - Conflicts :",sc)
    print("RR - Conflicts :",rc)

    s="<div class=\"titlespace\"><h1 id=\"title1\">CLR(1)</h1></div><div id=\"outbox1\">"

    s+="<div id=\"states\"><div id=\"titles12\"><h3>States</h3></div><div id=\"states1\">"
    
    
    j=0
    for i in sta:
        s+="<div class=\"state\"><div class=\"titles11\"><h4>State "+str(j)+"</h4></div>"
        j+=1
        for q in list(i.keys()):
            s+="<div class=\"item\"><div class=\"LHS\"><div class=\"LHS1\">"+q+"</div></div>"
            s+="<div class=\"RHS\"><div class=\"RHS1\">"
            for x in i[q][:-1]:
                s+=str(x)+","
            s+=str(i[q][-1])
            s+="</div></div></div>"
        s+="</div>"
    s+="</div></div>"

    s+="<table id=\"table1\"><caption>CLR(1) Table</caption><tr><th id=\"table1h1\"></th>"
    for i in T:
        s+="<th>"+i+"</th>"
    s+="<th id=\"table1h2\">$</th>"
    for i in NT[1:-1]:
        s+="<th>"+i+"</th>"
    s+="<th id=\"table1h5\">$</th>"
    s+="</tr>"
    
    
    qqqqq=list(tab.index)
    for i in qqqqq[:-1]:
        s+="<tr><th>"+str(i)+"</th>"
        for j in list(tab.loc[i]):
            s+="<td>"+j+"</td>"
        s+="</tr>"
    s+="<tr><th id=\"table1h3\">"+str(qqqqq[-1])+"</th>"
    for j in list(tab.loc[qqqqq[-1]][:-1]):
        s+="<td>"+j+"</td>"
    s+="<td id=\"table1h4\">"+tab.loc[qqqqq[-1]][-1]+"</td>"
    s+="</tr></table>"

    s+="<div id=\"conflicts1\"><h3>Conflicts</h3><div id= \"conflictslist\"><div class=\"absline1\"></div>"
    s+="<div class=\"titles1\"><div class=\"ftitle21\"><h5 class=\"ftitle11\">SR-CONFLICTS</h5></div><div class=\"ftitle21\"><h5 class=\"ftitle11\">RR-CONFLICTS</h5></div></div>"

    if(len(sc)+len(rc)>0):
        s+="<div class=\"lists1\"><ul class=\"list1\">"
        for i in list(sc.keys()):
            s+="<li>"+i+" : "+q1[i][0]
            for j in q1[i][1:]:
                s+=","+j
            s+="</li>"
        s+="</ul><ul class=\"list1\">"

        for i in list(rc):
            s+="<li>"+i+"</li>"
        s+="</ul></div></div></div>"

        print("The Given Grammer is Not an CLR(1) Grammar.")
        s+="<h4>The Given Grammar is Not an CLR(1) Grammar</h4></div>"
        return s
    s+="<div class=\"lists1\"><ul class=\"list1\"><li>No SR-Conflicts Exists</li></ul><ul class=\"list1\"><li>No RR-Conflicts Exists</li></ul></div></div><h4>The Given Grammar is an CLR(1) Grammar</h4></div>"


    if(len(inp)==0):
        s+="</div>"
        return s


    st=[0]
    qq=0
    i=0

    sti=[0]
    stz=[0]
    
    inp+='$'

    while(i<len(inp)):
        q = tdf[inp[i]][st[-1]]
        if(q[0]==-2):
            print("The Input String is Accepted by the Grammer")
            sti.append('$')
            sti.append('accept')
            stz.append(0)
            stz.append(0)
            qq=1    
            break
        if(q[0]!=-1):
            st.append(inp[i])
            st.append(q[0])
            sti.append(inp[i])
            sti.append(q[0])
            stz.append(0)
            stz.append(0)
            i+=1
            continue
        if(len(q[1])==1):
            for j in range(0,len(pr1[q[1][0][0]][1])):
                st.pop()
                st.pop()
                zzz=len(stz)-1
                while(stz[zzz]==1):
                    zzz-=1
                stz[zzz]=1
                stz[zzz-1]=1
            st.append(pr1[q[1][0][0]][0])
            st.append( tdf[st[-1]][st[-2]][0])
            sti.append(pr1[q[1][0][0]][0])
            sti.append(tdf[st[-2]][st[-3]][0])
            stz.append(0)
            stz.append(0)
            continue
        print("The Input String is Not Accepted by the Grammer")
        qq=1
        break

    
    s+="<div id=\"transitions\"><div class=\"item\">"
    j=0
    for i in sti:
        if(stz[j]==0):
            s+="<div class=\"LHS\"><div class=\"LHS2\">"
            s+=str(i)
            s+="</div></div>"
        else:
            s+="<div class=\"RHS\"><div class=\"RHS2\">"
            s+=str(i)
            s+="</div></div>"
        j+=1
    s+="</div>"

    if(qq==0):
        if(len(st)==0):
            s+="<div id=\"inpout\">The Input String is Accepted by the Grammer</div>"
            print("The Input String is Accepted by the Grammer")
        else:
            s+="<div id=\"inpout\">The Input String is Not Accepted by the Grammer</div>"
            print("The Input String is Not Accepted by the Grammer")
    else:
        s+="<div id=\"inpout\">The Input String is Accepted by the Grammer</div>"
    s+="</div>"
    return s   

