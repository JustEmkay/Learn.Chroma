import chromadb, uuid
import streamlit as st 


# create chroma client
cc = chromadb.Client()

# create collection 
collection = cc.get_or_create_collection( name = 'test_collection' )


if 'data' not in st.session_state:
    st.session_state.data = []

def clearSession() -> None:
    st.session_state.data = []

def createDict(input: str):
    
    tempDict : dict[str] = {
        'id' : str(uuid.uuid1()),
        'document' : input
    }
    
    st.session_state.data.append(tempDict)
    st.rerun()

def searchOnChroma(search: str) -> str:
    
    result = collection.query(
        query_texts= [search],
        n_results= 2
    )
    with st.expander('search result:', expanded= True):
        st.write(result)
    
def insertToChroma(data: list):
    
    ids : list = [ _['id'] for _ in data ]
    docs : list = [ _['document'] for _ in data ]
    
    try:
        collection.upsert(
            documents=docs,
            ids=ids
        )
        st.toast('Added to collection', icon= ":material/done_all:")
        
    except Exception as e:
        st.exception( e )
        
        
        
        


def main() -> None:
    
    #header
    st.header('Chromadb test', divider= True, anchor= False)
    input : str = st.text_input( "Enter something:" )
    if st.button('create doc'):
        if input:
            createDict(input)
            
    #subheader
    subh, bttn = st.columns([3,1], vertical_alignment= 'bottom')
    subh.subheader('Document', divider= True, anchor= False)
    bttn.button('clear all', on_click=clearSession, use_container_width= True)
    st.dataframe(st.session_state.data, use_container_width= True)
    
    #insert to chromadb
    if st.button( 'Insert into chromadb' ):
        insertToChroma( st.session_state.data)
    
    #subheader
    st.subheader( 'Search query using Chromadb', divider= True, anchor= False )
    subh2, bttn2 = st.columns([3,1], vertical_alignment='bottom')
    search = subh2.text_input("Enter a query to embed:", )
    if bttn2.button( 'Search query', use_container_width= True):
        searchOnChroma(search)
    else:
        st.caption("Type something to search")
    
    
    
    
    
    
    
#main 
if __name__ == '__main__':
    main()