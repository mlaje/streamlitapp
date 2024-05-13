# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Website Catalog")

st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)

st.write(
    """ Choose the clothes
    """
    )

#name_on_order = st.text_input('Name on Smoothie:')
#st.write('The name on your Smoothie will be:' , name_on_order)

cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("ZENAS_ATHLEISURE_DB.products.catalog_for_website").select(col('COLOR_OR_STYLE'), col('PRICE'))
pd_df = my_dataframe.to_pandas()
#st.dataframe(pd_df)
#st.dataframe(data=my_dataframe, use_container_width=True)

ropa = st.multiselect('Elegir ropa', my_dataframe)
import requests

if ropa:
    #st.write(ingredients_list)
    #st.text(ingredients_list)
    
    #ingredients_string = ''
    
    st.write(ropa)
    search_on = pd_df.loc[pd_df['COLOR_OR_STYLE'] == ropa, 'PRICE'].iloc[0]
    st.write(search_on)

    #for fruit in ingredients_list:
    #    ingredients_string +=  fruit.lstrip(" ") + ' '
    #    search_on=pd_df.loc[pd_df['FRUIT_NAME'] == fruit, 'SEARCH_ON'].iloc[0]
    #    st.write('The search value for ', fruit,' is ', search_on, '.')
    #    st.subheader(search_on + ' Nutrition Information')
    #    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + search_on)
    #    #st.text(fruityvice_response.json())
    #    fv_df = st.dataframe(data=fruityvice_response.json(), use_container_width=True)
    #st.write(ingredients_string)
    
    #my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order, order_filled)  
    #                 values('""" + ingredients_string + """','""" + name_on_order + """',""" + """false""" + """)"""

    #st.write(my_insert_stmt)
    #st.stop()
    
    #time_to_insert = st.button('Submit Order')
    
    #if time_to_insert:
    #    session.sql(my_insert_stmt).collect()
    #    st.success('Your Smoothie is ordered, ' + name_on_order + '!', icon="✅")
