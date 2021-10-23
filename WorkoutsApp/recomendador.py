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
    "ordenar lista de valores de la similitud coseno"
    sim_scores2 =sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
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
    val_1=(EjerciciosDF.at[(0),'calificacion'])*porce_cali + (val_alg[0][1])*porce_alg
    val_2= (EjerciciosDF.at[(1),'calificacion'])*porce_cali + (val_alg[1][1])*porce_alg
    val_alg_cal = [val_1,val_2]


    print("valores del algoritmo de cada ejercicio ->> ")
    print(val_alg)

    for i in range (2,len(EjerciciosDF.index)) :
          
        val = (EjerciciosDF.at[(i),'calificacion'])*porce_cali + (val_alg[i][1])*porce_alg
        val_alg_cal.append(val)
        print("Pruebas ->> ")
        print(i)
        print("Pruebas ->> ")
        print(val)

         

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



