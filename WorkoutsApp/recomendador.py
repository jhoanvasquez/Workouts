from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
import numpy  as np
import time
import string
from WorkoutsApp.models import Usuarios, Habilidades, Rangos, Ejercicios, EjerciciosUsuarios

def recomendador(id_user):
    EjerciciosDF = pd.DataFrame(list(EjerciciosUsuarios.objects.all().filter(id_usuario=id_user).values()))
       
    #Resetear index
    EjerciciosDF=EjerciciosDF.reset_index(drop=True)
    
    EjerciciosDF['Nexplicacion'] =EjerciciosDF['explicacion'].str.replace('[{}]'.format(string.punctuation), ' ', regex = True)
    tfidf = TfidfVectorizer(stop_words ='english')
    
    # "llenar con espacio vacio"

    EjerciciosDF['Nexplicacion']=EjerciciosDF['Nexplicacion'].fillna('') 
    tfidf_matrix = tfidf.fit_transform(EjerciciosDF['Nexplicacion'], y=None)

        
    # "matriz anterior con todas los valores de las similitudes de coseno"
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(EjerciciosDF.index,index=EjerciciosDF['descripcion']).drop_duplicates()


    return EjerciciosDF, cosine_sim, indices


def get_recommendations (EjerciciosDF, title, level, area_a, cosine_sim, indices):

    "obtener indice del ejercicio seleccionado, ej 0,1,2,3.."
    idx = indices[title]
    #print("tipo de cosa para volver lista enumerada" + str(type(cosine_sim[idx])))
    
    "obtener valores de la similitud coseno- array convertir a lista"
    sim_scores = list(enumerate(cosine_sim[idx]))
    "calcula suma de sim_cos + calificacion"
    sim_scores = list(enumerate(alg_Cal(sim_scores, EjerciciosDF)))
    print('sim_scores')
    print(sim_scores)
    "ordenar lista de valores de la similitud coseno"
    sim_scores2 =sorted(sim_scores, key=lambda x: x[0], reverse=True)
    
    "obtiene los valores del 1 al 6 del array ordenado"
    #sim_scores2 = sim_scores2[1:6]
    
    #print("valores de pos 2 a la pos 5" + str(sim_scores2))
    "obtiene los indices de cada elemento del array"
    movie_indices = [i[0] for i in sim_scores2 ]
    #print("indices de peliculas obtenidos" + str(movie_indices))
    
    "validar si el indice tiene el mismo level y area ingresado"
    "si es asi, agregarlo al sim_scores2 en el orden que viene ya"
    movie_indices2 = []

    for d in range (len(movie_indices)-1):

        if(EjerciciosDF.iloc[movie_indices[d]]['id_rango_id'] == level):
        #and (Ejercicios.iloc[movie_indices[d]]['id_area']  == area_a)):
            movie_indices2.append(movie_indices[d])
    
    #print(movie_indices2)
    movie_indices2 = movie_indices2[1:6]

    return EjerciciosDF['id_ejercicios_id'].iloc[movie_indices2]



"se calcula la suma de algoritmo + calificacion, se recibe los % de sim_cos"
def alg_Cal(val_alg, EjerciciosDF):
    # global EjerciciosDF
    "% para conformar rangos de 0 a1"
    porce_alg = 0.5
    porce_cali = 0.1
    #val_1=(EjerciciosDF.at[(0),'calificacion'])*porce_cali + (val_alg[0][1])*porce_alg
    #val_2= (EjerciciosDF.at[(1),'calificacion'])*porce_cali + (val_alg[1][1])*porce_alg
    #val_alg_cal = [val_1,val_2]
    val_alg_cal = []

    opcion=0
    
    #print("tamano de val_calificacion")
    #print(type(val_alg[0][1]))
    #print(val_alg[0][1])
    # print("ejercicios ")
    # print(EjerciciosDF)
    # print("ejercicios TAMANIO")
    # print(len(EjerciciosDF.index))
    

    if(type(val_alg[0][1]) == np.ndarray):
        # print("es array")
        # print(val_alg[0][1])
        # print(len(val_alg[0][1]))
        # print("PRIMER VALOR DEL ARRAY")
        # print(val_alg[0][1][0])
        opcion=1
    
    if(type(val_alg[0][1]) == np.float64):
        # print("es un solo valor, y es float")
        # print(val_alg)
        opcion=2

    if(opcion == 1):

        for i in range (0,len(EjerciciosDF.index)) :
            val11 = (EjerciciosDF.at[(i),'calificacion'])*porce_cali
            #val22 = (val_alg[i][1])*porce_alg
            val22 = (val_alg[0][1][i])*porce_alg
            #val = (EjerciciosDF.at[(i),'calificacion'])*porce_cali + (val_alg[i][1])*porce_alg
            val = val11 + val22
            val_alg_cal.append(val)
            # print("prueba ->")
            # print(i)
            # print("prueba val11->")
            # print(val11)
            # print("prueba val22->")
            # print(val22)
            # print("prueba val->")
            # print(val)

    if(opcion == 2):
        for i in range (0,len(EjerciciosDF.index)) :
            val11 = (EjerciciosDF.at[(i),'calificacion'])*porce_cali
            val22 = (val_alg[i][1])*porce_alg
            #val = (EjerciciosDF.at[(i),'calificacion'])*porce_cali + (val_alg[i][1])*porce_alg
            val = val11 + val22
            val_alg_cal.append(val)
            # print("prueba ->")
            # print(i)
            # print("prueba val11->")
            # print(val11)
            # print("prueba val22->")
            # print(val22)
            # print("prueba val->")
            # print(val)

    return val_alg_cal

#Variables de prueba
# EjerciciosDF, cosine_sim, indices = recomendador()
# print(EjerciciosDF['id_rango_id'])
# ind=1
# titulo = str(EjerciciosDF.iloc[ind]['descripcion'])
# nivel = EjerciciosDF.iloc[ind]['id_rango_id']
# a_area = EjerciciosDF.iloc[ind]['id_area_id']

# titulo2 = str(Entrenos.iloc[1]['area']['intensidad'])
# print("seleccionaste: "+ titulo+ " y tu recomendaciones son: ")
# print("nivel: "+ str(nivel)+ " area: "+ str(a_area))
# print(get_recommendations(EjerciciosDF, titulo, nivel, a_area, cosine_sim, indices))



