import pandas as pd, json
df=pd.read_csv('/mnt/user-data/uploads/flipkart_com-ecommerce_sample.csv').dropna(subset=['uniq_id','discounted_price','retail_price']).reset_index(drop=True)
df['ts']=pd.to_datetime(df.crawl_timestamp.str[:19]).dt.to_period('M').astype(str)
cat=df.product_category_tree.str.strip('[]"').str.split(' >> ')
df['c1']=cat.str[0].fillna('Other'); df['c2']=cat.str[1].fillna('Other'); df['brand']=df.brand.fillna('Unbranded')
df['rt']=pd.to_numeric(df.overall_rating,errors='coerce').fillna(0)
def enc(col):
    a=sorted(df[col].unique()); return a,{v:i for i,v in enumerate(a)}
M,mi=enc('ts');C,ci=enc('c1');S,si=enc('c2');B,bi=enc('brand')
R=[[mi[a],ci[b],si[c],bi[d],int(e),int(f),float(g)] for a,b,c,d,e,f,g in zip(df.ts,df.c1,df.c2,df.brand,df.retail_price,df.discounted_price,df.rt)]
P=[n[:80] for n in df.product_name.fillna('')]
data=json.dumps(dict(M=M,C=C,S=S,B=B,P=P,R=R),separators=(',',':')).replace('</','<\\/')
html=open('template.html').read().replace('/*CHARTJS*/',open('node_modules/chart.js/dist/chart.umd.js').read()).replace('/*DATA*/',data)
open('/mnt/user-data/outputs/flipkart_sales_dashboard.html','w').write(html)
print(len(R),len(html)//1024,'KB',M)
df[['uniq_id','product_name','product_category_tree','retail_price','discounted_price','brand','overall_rating','crawl_timestamp']].head(40).to_csv('raw_head.csv',index=False)
