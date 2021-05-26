import streamlit as st
import pandas as pd
import codecs
import dtale
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import sweetviz as sv
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


def st_display_sweetviz(report_html,width=1000,height=500):
	report_file = codecs.open(report_html,'r')
	page = report_file.read()
	components.html(page,width=width,height=height,scrolling=True)

st.title("WELCOME TO AUTOMATED APP")

footer_html="""

"""



def main():
    classifer = ["Linear regression", "logistic regression", "XG Boost", "DT", "Random forest"]
    choice = st.sidebar.selectbox("Classifer", classifer)
    menu=["Home","Pandas Profile","Sweetviz","DTale","About"]
    choice=st.sidebar.selectbox("Menu",menu)


    if choice=="Pandas Profile":
        st.subheader("Automated EDA with Pandas Profiling")

        data_file=st.file_uploader("Upload CSV",type=['csv'])
        if data_file is not None:
            df=pd.read_csv(data_file)
            st.dataframe(df.head())
            profile=ProfileReport(df)
            st_profile_report(profile)


    elif choice=="Sweetviz":
        st.subheader("Automated EDA with Sweetviz")
        data_file = st.file_uploader("Upload CSV", type=['csv'])
        if data_file is not None:
            df = pd.read_csv(data_file)
            st.dataframe(df.head())
            if st.button("Generate Sweetviz Report"):\
                    report=sv.analyze(df)
            report.show_html()
            st_display_sweetviz("SWEETVIZ_REPORT.html")

    elif choice=="DTale":
        st.subheader("Automated EDA with DTale")
        data_file = st.file_uploader("Upload CSV", type=['csv'])
        if data_file is not None:
            df = pd.read_csv(data_file)
            st.dataframe(df.head())
            if st.button("Generate DTale Report"): \
                    d = dtale.show(df)
            d.open_browser()
            d._data_id  # the process's data identifier
            d._url  # the url to access the process
            d2 = dtale.get_instance(d._data_id)  # returns a new reference to the instance running at that data_id
            dtale.instances()  # prints a list of all ids & urls of running D-Tale sessions





    elif choice=="About":
        st.subheader("About App")
        st.subheader("Pandas-Profiling")
        st.subheader("Pandas profiling is an open-source Python module with which we can quickly do an exploratory data analysis with just a few lines of code. Besides, if this is not enough to convince us to use this tool, it also generates interactive reports in a web format that can be presented to any person, even if they don’t know to program.In short, what pandas profiling does is save us all the work of visualizing and understanding the distribution of each variable. It generates a report with all the information easily available.")

        st.subheader("Sweetviz")
        st.subheader("Sweetviz is an open-source Python library that generates beautiful, high-density visualizations to kickstart EDA (Exploratory Data Analysis) with just two lines of code. Output is a fully self-contained HTML application.The system is built around quickly visualizing target values and comparing datasets. Its goal is to help quick analysis of target characteristics, training vs testing data, and other such data characterization tasks.")

        st.subheader("DTale")
        st.subheader("D-Tale is the combination of a Flask back-end and a React front-end to bring you an easy way to view & analyze Pandas data structures. It integrates seamlessly with ipython notebooks & python/ipython terminals. Currently this tool supports such Pandas objects as DataFrame, Series, MultiIndex, DatetimeIndex & RangeIndex.")


    else:
        st.subheader("Home")







        html_temp = """
        		<div style="background-color:royalblue;padding:10px;border-radius:10px">
        		<h1 style="color:white;text-align:center;">Abijith EDA & Machine leaninng application</h1>
        		</div>
        		"""
        components.html(html_temp)
        components.html("""
            
            <style>
			
			/* Next & previous buttons */
			.prev, .next {
			  cursor: pointer;
			  position: absolute;
			  top: 50%;
			  width: auto;
			  padding: 16px;
			  margin-top: -22px;
			  color: white;
			  font-weight: bold;
			  font-size: 18px;
			  transition: 0.6s ease;
			  border-radius: 0 3px 3px 0;
			  user-select: none;
			}
			/* Position the "next button" to the right */
			.next {
			  right: 0;
			  border-radius: 3px 0 0 3px;
			}
			/* On hover, add a black background color with a little bit see-through */
			.prev:hover, .next:hover {
			  background-color: rgba(0,0,0,0.8);
			}
			/* Caption text */
			.text {
			  color: #f2f2f2;
			  font-size: 15px;
			  padding: 8px 12px;
			  position: absolute;
			  bottom: 8px;
			  width: 100%;
			  text-align: center;
			}
			/* Number text (1/3 etc) */
			.numbertext {
			  color: #f2f2f2;
			  font-size: 12px;
			  padding: 8px 12px;
			  position: absolute;
			  top: 0;
			}
			/* The dots/bullets/indicators */
			.dot {
			  cursor: pointer;
			  height: 30px;
			  width: 15px;
			  margin: 0 2px;
			  background-color: #bbb;
			  border-radius: 100%;
			  display: inline-block;
			  transition: background-color 0.6s ease;
			}
			.active, .dot:hover {
			  background-color: #717171;
			}
			/* Fading animation */
			.fade {
			  -webkit-animation-name: fade;
			  -webkit-animation-duration: 1.5s;
			  animation-name: fade;
			  animation-duration: 1.5s;
			}
			@-webkit-keyframes fade {
			  from {opacity: .4} 
			  to {opacity: 1}
			}
			@keyframes fade {
			  from {opacity: .4} 
			  to {opacity: 1}
			}
			/* On smaller screens, decrease text size */
			@media only screen and (max-width: 300px) {
			  .prev, .next,.text {font-size: 11px}
			}
			</style>
			</head>
			<body>
			    

<div class="mySlides fade">

  <img src="https://wordstream-files-prod.s3.amazonaws.com/s3fs-public/styles/simple_image/public/images/machine-learning1.png?SnePeroHk5B9yZaLY7peFkULrfW8Gtaf&itok=yjEJbEKD" style="width:100%",object-fit:contain">
  

</div>

<div class="mySlides fade">
  
  <img src="https://f.hubspotusercontent00.net/hubfs/53/data%20visualization%20copy.jpg" style="width:75%,object-fit:contain">
 
</div>
			<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
			<a class="next" onclick="plusSlides(1)">&#10095;</a>
			</div>
			<br>
			<div style="text-align:center">
			  <span class="dot" onclick="currentSlide(1)"></span> 
			  <span class="dot" onclick="currentSlide(2)"></span> 
			  <span class="dot" onclick="currentSlide(3)"></span> 
			</div>
			<script>
			var slideIndex = 1;
			showSlides(slideIndex);
			function plusSlides(n) {
			  showSlides(slideIndex += n);
			}
			function currentSlide(n) {
			  showSlides(slideIndex = n);
			}
			function showSlides(n) {
			  var i;
			  var slides = document.getElementsByClassName("mySlides");
			  var dots = document.getElementsByClassName("dot");
			  if (n > slides.length) {slideIndex = 1}    
			  if (n < 1) {slideIndex = slides.length}
			  for (i = 0; i < slides.length; i++) {
			      slides[i].style.display = "none";  
			  }
			  for (i = 0; i < dots.length; i++) {
			      dots[i].className = dots[i].className.replace(" active", "");
			  }
			  slides[slideIndex-1].style.display = "block";  
			  dots[slideIndex-1].className += " active";
			}
			</script>
			
			
			""")

if __name__ == '__main__':
	main()



