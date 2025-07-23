import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_performances(path,j,k,ax,title='None'):
    df= pd.read_csv(path)
    #df['total_threads']=df['n_workers']*df['n_threads'] * 4
    df['time']=np.round((df['time1']+df['time2']+df['time3'])/3,2)
    df['std']=np.round(np.std([df['time1'],df['time2'],df['time3']],axis=0),2)
    df['config']=df['n_workers'].astype(str) + 'proc. - ' + df['n_threads'].astype(str)+ ' thr.'
    #num_threads=str(df['total_threads'][0])
    num_threads=str(df['n_workers'].values[0]*df['n_threads'].values[0]*4)

    results=df.drop(columns=['n_workers','n_threads','time1','time2','time3']) #,'total_threads'])

    indexes=np.unique(np.array(results['config'].values)).tolist()

    for i in range(len(indexes)):
        data=results.drop(columns='config').loc[(np.where(results['config']==indexes[i])[0]).tolist()].to_numpy()
        ax[j,k].errorbar(x=range(len(data[:,0])),y=data[:,1],yerr=data[:,2],label=f'{indexes[i]}',fmt='o-')
        
    if title=='None': ax[j,k].set_title(f'Execution Times with {num_threads} total threads')
    else: ax[j,k].set_title(title+f', {num_threads} thr.')
    ax[j,k].set_xlabel('Partitions')
    ax[j,k].set_xticks(range(len(data[:,0])))
    ax[j,k].set_xticklabels(np.array(data[:,0],dtype=int))
    ax[j,k].set_ylabel('Time (s)')
    ax[j,k].legend()


def heat(path):
    df= pd.read_csv(path)
    df['total_threads']=df['n_workers']*df['n_threads'] * 4
    df['time']=(df['time1']+df['time2']+df['time3'])/3
    df['time']=np.round(df['time'],2)
    df_print=df.drop(['n_workers','n_threads','time1','time2','time3'],axis=1)
    partitions=np.unique(np.sort(np.array(df_print['n_partitions'])))
    threads=np.unique(np.sort(np.array(df_print['total_threads'])))

    #print('indexes of the grid: ',partitions,threads)
    matrix=np.zeros((len(partitions),len(threads)))
    data=df_print.to_numpy()
    #print(data)
    for i in range(len(partitions)):
        for j in range(len(threads)):
            for k in range(data.shape[0]):
                if data[k,0]==partitions[i] and data[k,1]==threads[j]:
                    if matrix[i,j] !=0:
                        if matrix[i,j]>data[k,2]: matrix[i,j]=np.round(data[k,2],2) #se ho un risultato minore, lo sostituisco
                    else:matrix[i,j]=np.round(data[k,2],2) 
    #print('Result matrix: \n',matrix)

    ax=sns.heatmap(matrix,cmap='Blues_r',vmin=63,vmax=103,annot=True,xticklabels=threads,yticklabels=partitions, fmt=".0f")
    ax.set(title='Operation time (seconds)' ,xlabel='Threads',ylabel='Partitions')


def plot_performances_2(path,ax,title,j=100,k=100):
    if (j!=100 and k!=100): ax=ax[j,k] #for 2D subplots
    
    df= pd.read_csv(path)
    df['time']=np.round((df['time1']+df['time2']+df['time3'])/3,2)
    df['std']=np.round(np.std([df['time1'],df['time2'],df['time3']],axis=0),2)
    if (j==100 and k==100): df['n_partitions']=df['true_partitions']
    df['config']=df['n_workers'].astype(str) + 'proc. - ' + df['n_threads'].astype(str)+ ' thr.'
    
    if (j==100 and k==100): df_to_plot=df.drop(columns=['n_workers','n_threads','time1','time2','time3','true_partitions','chunck_sizes'])
    else: df_to_plot=df.drop(columns=['n_workers','n_threads','time1','time2','time3'])#,'true_partitions','chunck_sizes'])
    
    indexes=np.unique(np.array(df_to_plot['config'].values)).tolist()
    partitions=(df['n_partitions'].values)
    partitions=(np.unique(sorted(partitions)))

    for i in range(len(indexes)):
        data=df_to_plot.drop(columns='config').loc[(np.where(df_to_plot['config']==indexes[i])[0]).tolist()]
        x=([int(np.argwhere(partitions==i)[0][0])+1 for i in data['n_partitions'].values])
        index=np.argsort(x)
        data=data.to_numpy()

        ax.errorbar(x=sorted(x),y=data[index,1],yerr=data[index,2],label=f'{indexes[i]}',fmt='o-')
        if (j==100 and k==100): ax.set_title(title, weight='bold')
        else: ax.set_title(title)
        ax.set_xlabel('Partitions')
        ax.set_xticks(np.arange(1,len(partitions)+1,1))
        ax.set_xticklabels(np.array(partitions,dtype=int))
        ax.set_ylabel('Time (s)')
        ax.legend()
        