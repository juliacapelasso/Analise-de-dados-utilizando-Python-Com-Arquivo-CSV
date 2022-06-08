#!/usr/bin/env python
# coding: utf-8

# In[ ]:


LIMPEZA E TRATAMENTO DE DADOS A PARTIR DE UM ARQUIVO CSV UTILIZANDO PYTHON


# In[2]:


#Importar as bibliotecas que serão utilizadas
import pandas as pd
import statistics as sts
import seaborn as srn


# In[3]:


#Carregar o arquivo que será utilizado nessa análise
dataset = pd.read_csv("tempo.csv", sep=";")
dataset.head()


# In[4]:


#Determinar o tamanho da tabela
dataset.shape


# In[33]:


#Tratar a coluna "Aparencia"
#Contar e ver qual item eu tenho mais na coluna "Aparencia"

agrupar = dataset.groupby(['Aparencia']).size()
agrupar

# Através do resultado acima, descobrimos que há um item diferente de "sol", "nublado" e "chuva".


# In[41]:


# Incluir esse item "menos" na aparencia "nublado"

agrupar_de_novo = dataset.groupby(['Aparencia']).size()
dataset.loc[dataset['Aparencia'] ==  'menos', 'Aparencia'] = "nublado"
agrupar_de_novo = dataset.groupby(['Aparencia']).size()
agrupar_de_novo


# In[48]:


#Agora tratar os dados da coluna "Temperatura":
#Verificar se há algum dado fora do limite de temperatura (<135ºF ou >130ºF):
dataset['Temperatura'].describe
dataset.loc[(dataset['Temperatura']< -130) | (dataset['Temperatura']> 130)]


# In[46]:


#Temos uma temperatura de 1220º, ou seja, um outlier
mediana = sts.median(dataset["Temperatura"])
mediana


# In[47]:


#Substituir o valor absurdo pela mediana
dataset.loc[(dataset['Temperatura']< -130) | (dataset['Temperatura']> 130), "Temperatura"] = mediana


# In[ ]:


#Verificar se ainda existem valores fora do domínio:
dataset.loc[(dataset['Temperatura']< -130) | (dataset['Temperatura']> 130), "Temperatura"]
#Não há, logo, os dados foram tratados


# In[51]:


# Tratar a coluna "Umidade":
#Verificar se há algum número fora do intervalo 0-100:
dataset['Umidade'].describe
dataset.loc[(dataset['Umidade']< 0) | (dataset['Umidade']> 100)]


# In[ ]:


#Há uma umidade de 200 que precisa ser corrigida
mediana = sts.median(dataset["Umidade"])
mediana


# In[ ]:


#Substituir o valor absurdo pela mediana
dataset.loc[(dataset['Umidade']< 0) | (dataset['Umidade']> 100), "Umidade"] = mediana


# In[ ]:


#Verificar se ainda existem valores fora do domínio:
dataset.loc[(dataset['Umidade']< 0) | (dataset['Umidade']> 100), "Umidade"]

#Não há, logo, os dados foram tratados


# In[35]:


# Tratar a coluna "Jogar":
#Verificar se há algum carácter fora da lógica sim/não:
agrupar = dataset.groupby(['Jogar']).size()
agrupar

#Não há nada fora de sim/não nessa coluna


# In[53]:


#Por fim, analisar se há dados NAN
dataset.isnull().sum()


# In[57]:


#Remover os dados NAN da tabela.
dataset.dropna()


# In[ ]:




