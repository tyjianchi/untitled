
import xlrd
import pandas as pd

class gl_mode2():

    def pd_read(self,filepath):

        #定义字段顺序
        col_list=['acct_book','date','vou_no','desc','sub_code','sub_name','currency',
                  'debit_org_amt','debit_loc_amt','credit_org_amt','credit_loc_amt']

        #读取文件到DataFrame
        df = pd.read_excel(filepath)

        #数据清洗，排除多余数据
        df2=pd.DataFrame(df[6:-2])

        #根据字段顺序重命名列名
        df2.columns=col_list

        #过滤需要的字段
        df3=df2.filter(items=['sub_name','desc','debit_org_amt','credit_org_amt'])

        #过滤需要的行
        bool=df3['sub_name'].str.contains('利息调整|可供出售.+公允价值变动')
        df4=df3[bool]

        #数值字段清洗，去空格，去逗号
        for i in range(2,len(df4.columns)):
            for z in range(0,len(df4.index)):
                for y in df4.iloc[z:z+1,i]:
                    if not isinstance(y,(int,float)):
                        df4.iloc[z:z + 1, i]=y.replace(',', '').replace(' ', '')

        #数值字段（object）类型转换为float
        df4.debit_org_amt=pd.to_numeric(df4['debit_org_amt'])
        df4.credit_org_amt = pd.to_numeric(df4['credit_org_amt'])

        #字符串正则提取，匹配SQ\d+
        df4.desc=df4.desc.str.extract(r'(SQ\d+)')

        #字符串正则替换
        df4.sub_name = df4.replace(regex={r'.+利息调整':'利息调整',r'.+公允价值变动':'公允价值'})

        #根据sub_name字段聚合汇总
        df5=(df4.groupby(['sub_name','desc']).agg({'debit_org_amt': 'sum', 'credit_org_amt': 'sum'}).eval('Total_AMT = debit_org_amt - credit_org_amt'))

        #因为聚合汇总后，会导致groupby字段变成索引列，用reset_index可以重建索引
        df5=df5.reset_index()

        #行转列
        df_pivoted=df5.pivot(index='desc',columns='sub_name',values='Total_AMT')

        #写入文件
        df_pivoted.to_excel(r'C:\Elven_Code\gl_model2\SQ_TOTAL.xlsx', sheet_name='Data1')

gl=gl_mode2()
#gl.rd_excel(r"C:\Elven_Code\gl_model2\SQ000001201806210001.xls")
gl.pd_read(r"C:\Elven_Code\gl_model2\总账_序时账_原本_NEW.xls")