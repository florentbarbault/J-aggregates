import matplotlib.pyplot as plt
fichier = open("script.cpptraj.inp", "a")
fichier.write ("parm ../*.prmtop \n")
fichier.write ("trajin ../prodHMR.12.nc 1 last 5 \n")
r_i=-2
r_j=-1
# loops
for i in range(1,161):
        for j in range (i+1,161):
                    r_i=r_i+2
                    r_j=r_j+2
                    distanceout="DATA/distance"+str(i)+"-"+str(j)+".dat"
                    angleout="DATA/angle"+str(i)+"-"+str(j)+".dat"
                    select="@C1,C2,C3,C4,C9,C10,C11,C14,C15,C16,C17,C18,C19,CG,CD1,CD2,CE1,CE2,CZ" # aromatic atoms for Fmoc, Phe et pTyr
                    cpp_distance="distance "+distanceout+" :"+str(i)+select+" :"+str(j)+select+" out "+distanceout+" \n"
                    vec1="vector v"+str(r_i)+" corrplane :"+str(i)+select+" \n"
                    vec2="vector v"+str(r_j)+" corrplane :"+str(j)+select+" \n"
                    cpp_angle="vectormath vec1 v"+str(r_i)+" vec2 v"+str(r_j)+" dotangle out "+angleout+" \n" 
                    fichier.write(cpp_distance)
                    fichier.write(vec1)
                    fichier.write(vec2)
                    fichier.write(cpp_angle)
# end of loops                                                                                             
fichier.write("run \n")
fichier.write("quit \n")
fichier.close()
print ("You should now execute J-AGGREGATES.sh")






