from sklearn.cluster import KMeans
import pandas as pd
import json
import numpy as np
from scipy.spatial import distance
from sklearn.manifold import TSNE



"""CHANGE IT. THIS IS WHERE USER INPUTS WERE GIVEN, SHOULD BE IN THE FORMAT OF LIST"""

user_input_vector= [1 , 0. , 0. , 0. , 0. , 0.5, 0. , 0.5, 1. , 0. , 0. , 0. , 0. ,
        0. , 0. , 0. , 0. , 0. , 0. , 0. , 0.5, 0.5, 0.5, 0. , 0. , 0.5,
        0.5, 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. ,
        0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. ,
        0. , 0. , 0. , 0. , 1. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. ,
        0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. ,
        0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0.5 , 0. , 0. , 0. , 0. ,
        0. , 0. , 1. , 1. , 1. , 1. , 1. , 0. , 0. , 0. , 0. , 0. , 0. ,
        0. , 0. , 0. , 0. , 0. , 0. , 1. , 0. , 0. , 0. , 0. , 0. , 0. ,
        0. , 0. , 0. , 0. , 0. , 0. , 1. , 0. , 0. , 0. , 0. , 0. , 0. ,
        0. , 0. , 0. , 0. , 0. , 0. , 0.3 , 0.3 , 0. , 0. , 0. , 0. , 0. ,
        0. , 0. ]


""" First function """
def read_data(file_path):
    df = pd.read_csv(file_path, header=[0,1], index_col=0)
    return df


""" Second function"""
def do_TSNE(user_input_vector,data,output_dims, verbose=0, perplexity=30):
    """
    Reduce the dimensionaly from data.colmns into to output_dims
    Returns a numpy array of (len(data), output_dims)
    """
    df_uservector=pd.DataFrame(np.array(user_input_vector).reshape(-1,len(user_input_vector)))#flat to row pd dataframe
    dataframe = pd.concat([data, df_uservector]).fillna(0).reset_index(drop=True)
    tsne = TSNE(n_components=output_dims, random_state=0, verbose=verbose, perplexity=perplexity)
    data_2d = tsne.fit_transform(dataframe)
    data_2d_df= pd.DataFrame(data_2d,columns=['x','y'])

    dataframe=dataframe.drop(index=220).reset_index(drop=True)

    return data_2d_df #contains the user input and user input is at the bottom

""" Thrid function"""
def seperate_user_input(img_name,train_tsne_final): #this function seperates the tsne results of images and tsne result of user input
    results_original = do_TSNE(user_input_vector,train_tsne_final, 2)
    image_tsne= results_original[:220] # tsne results of all the images
    image_tsne['img']=img_name
    user_tsne=results_original[220:] #tsne results of user input
    return image_tsne,user_tsne


"""Other stuff """
def kmeans_predict(df, n_cluster, tsne_x, tsne_y): #predict the cluster of user_input after tsne processing
    km_df=df[["x","y"]].to_numpy()
    user_input=[[tsne_x,tsne_y]]
    df_user_input= pd.DataFrame(user_input)
    kmeans = KMeans(n_clusters=n_cluster, random_state = 0)
    kmeans.fit(km_df)
    user_cluster = kmeans.predict(df_user_input)
    return user_cluster

def kmeans_df_labels(df, n_cluster): #create a tsne result dataframe with Kmeans cluster label

    km_df=df[["x","y"]].to_numpy()
    Kmeans_result=KMeans(n_clusters=n_cluster, random_state = 0).fit(km_df)
    labels= Kmeans_result.labels_
    df['labels']=labels

    return df

""" fourth function"""
def user_cluster_distance(df, n_cluster, tsne_x, tsne_y): #combine the function kmeans_df_labels with kmeans_predict
    user_cluster = kmeans_predict(df, n_cluster, tsne_x, tsne_y)
    a=user_cluster.tolist()
    df=kmeans_df_labels(df, n_cluster)
    rows = df.loc[df['labels']==a[0]] #search for cluster that match with user's predicted cluster
    array_df=rows.to_numpy() #convert to array for iteration
    distance_list=[]
    for i in array_df:
        Euclidean_distance=distance.euclidean((i[0],i[1]),(tsne_x, tsne_y))
        distance_list.append(Euclidean_distance)

    new_array= pd.DataFrame(array_df, columns=['x','y','img_name','cluster'])#convert to df again
    new_array['distance Euclidean']=distance_list
    similar_image=new_array.nsmallest(10, 'distance Euclidean').reset_index(drop=True) #you can define how many images you want to return here
    return list(similar_image['img_name']+'.jpg')

def final_cluster():
    """ Calls first function"""
    df_01= read_data('./static/Attributes/NOWHERE_DATASET.csv')
    img_name=df_01['Name']

    """Load TSNE """
    train_df=pd.read_csv('./static/Attributes/tsne_train.csv')
    train_df_1= train_df.drop(['Unnamed: 0'],axis=1)
    train_tsne_final=train_df_1.drop(index=0).reset_index(drop=True)



    """Calls second function """
    results_original = do_TSNE(user_input_vector,train_tsne_final, 2)

    """ Calls thrid function """
    image_and_user=seperate_user_input(img_name,train_tsne_final)

    cluster_df_image=image_and_user[0] #updated image dataframe from tsne
    tsne_x= image_and_user[1]['x'].tolist()[0]
    tsne_y=image_and_user[1]['y'].tolist()[0]

    """ Calls fourth function"""
    """tsne_x and tsne_y will be changed automatically, cluster we need to define ourselves. You only need to change the user input"""
    image_list = user_cluster_distance(cluster_df_image, 6, tsne_x,tsne_y)

    results = []
    image_names = []

    for image in image_list:
        image_names.append(image[:-4])
        image = '../static/pictures/' + image
        results.append(image)

    return results, image_names
