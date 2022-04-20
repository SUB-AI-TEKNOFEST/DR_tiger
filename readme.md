# Dr_Tiger
**Contributers and Contact Information: **

Utku Sağlam saglmutku@gmail.com

Beytullah Aksoy beytullah557@gmail.com

Alper Özcan alper.ozcan@gmail.com

**Problem Statement:**
GRAPH FOR BETTER HEALTH
Find Novel Drug Treatments

**Description**:
Diseases are a complex set of phenomena that have various relationships with drugs, cells, and organisms. Each of these relationships creates more complexity to find the proper drug for the disease. To find the proper drug for the disease, designing and developing it is an expensive process. As we know, drugs can cure a variety of diseases but usually, they use just for one or two diseases. People are inclined to use drugs not according to the prospectus to solve their diseases. Unapproved use of an approved drug is often called “off-label” use. Off-label usage of drugs has increased dramatically in the last ten years. 

With advanced machine learning techniques, we are able to do drug repurposing for different diseases. These can solve the issues related to off-label usage and reproducing drugs that cost billions of dollars.

The aim of our project is to provide drug repurposing using graph and machine learning. Drug repurposing is a strategy for identifying new uses for approved or investigational drugs that are outside the scope of the original medical indication. Given the high attrition rates, substantial costs and slow pace of new drug discovery and development, repurposing of 'old' drugs to treat both common and rare diseases is increasingly becoming an attractive proposition because it involves the use of de-risked compounds, with potentially lower overall development costs and shorter development timelines. Various data-driven and experimental approaches have been suggested for the identification of repurposable drug candidates.
In order to obtain high accuracy in these studies, large and comprehensive data should be used. We used the DRKG dataset in this project. This dataset contains more than 5.8 million data, which is kept as a graph, and therefore, a database that can perform fast processing and is suitable for machine learning projects is needed. TigerGraph is very suitable for these purposes.


**Our project is the most Impactful in solving a real world problem**:
Dr_tiger helps the pharmaceutical industry to reuse drugs for other diseases and assists in clinical studies in the discovery of drugs against diseases.
Reusing drugs to treat both common and rare diseases offers the advantage of working with compounds with reduced risk. Because of its cost-effectiveness and reduced timetable, reusing drugs for new indications represent a method for finding rare disease treatments that have advantages over conventional drug development. An example is Pfizer Rapamune® (sirolimus), which was approved to prevent transplant rejection but was also the first approved drug for the rare genetic lung disease lymphangioleiomyomatosis.
Dr_tiger aims to benefit all humanity as it affects the health sector.
The application contributes to all structures of society by providing benefits to both high and low-income economies, as the reuse of drugs reduces drug production costs.
“By drug repurposing, we’ve tested a lot of things that, with less urgency, would have never gone into clinical trials,” says Matthew Hall, NCATS’s acting director of biology and group leader of the Early Translation Branch. 
In addition to economic reasons, we believe that Dr_tiger will increase the scope of future clinical studies.

**Our project is the most Innovative use case of graph**:
Innovations in the pharmaceutical industry have become more important in the last decades. We aimed to create an innovative and easy use application with Dr_Tiger. The first innovation is that we offer a basic user interface and a good user experience. The application user interface is not complex and a researcher who wants to find related drugs for a specific disease can easily use it without any prior knowledge. Another innovation that Dr_tiger offers is using pre-trained and topological link prediction parameters. Using pre-trained vectors gives a faster train time also, using topological link prediction parameters with a graph data science library in the TigerGraph increase the accuracy.
Dr_tiger is an application that offers a complete solution for the pharmaceutical industry and academic research.

**Our project is the most - Ambitious and complex graph**:
Drug repurposing is hard to do because it needs big datasets, relations, and good machine learning knowledge. At the moment, we use almost 6000 diseases and 5.8 million rows for repurposing drugs. Furthermore,
there are different types of vertices like genes, compounds, symptoms, etc. The application uses pre-trained vectors to overcome training issues and it uses Tigergraph data science library functionalities like topological link prediction queries. 
At the moment, we believe that we offer a real-world solution for both industry and academia. However, there is a space for improvement in our application.
Dr_tiger is an application that offers applicable solutions for drug repurposing and it is ready to move next step!:

**Our project is the most Applicable graph solution**:
Our solution can have effects on different industries and also it can be used in both academia and industry. For instance, Scientists who conduct clinical studies will be able to select the disease they want to study from the Dr_tiger website as long as it is in our dataset and continue their studies based on the predictions made. Also, people who are working on graphs will be able to examine the topological results that are found, and they will be able to examine graphs more easily with visualization.

We have presented our solution ready for use in the real world. Therefore, it will be a short and easy process for organizations to adapt to it. It has already almost 6000 diseases and different vertices from genes to symptoms.

The total trade volume of the pharmaceutical industry in the world was over US$ 1.42 trillion. Due to the drug repurposing costs in the pharmaceutical industry, firms are making investments in innovative and easy-to-use solutions. Our solution uses advanced machine learning techniques and TigerGraph power as a database service. It offers an innovative SaaS product that can be used by all ages.


- **Data**:
  We used the DRKG dataset.
- **Technology Stack**:
  Flask, JS, torch, pytorch, pytigergraph, pandas, torchdrug, matplotlib, uvicorn.
- **Visuals**:
-  https://www.youtube.com/watch?v=5r-vlL_daG4
![Ekran Resmi 2022-04-14 00 41 19](https://user-images.githubusercontent.com/58150504/163575916-51990326-055e-4621-9a22-8952c5e839e9.png)

![Ekran Resmi 2022-04-14 00 41 26](https://user-images.githubusercontent.com/58150504/163575952-970e947b-4933-4f16-a17a-f4b76a2709fd.png)
![Ekran Resmi 2022-04-20 12 41 28](https://user-images.githubusercontent.com/58150504/164199961-f9be9a7d-cfaf-44dc-9a7f-1d3e0a650fe5.png)


## Dependencies
  Installation part steps have to be followed.

## Installation

1. Clone repository
  * git clone git@github.com:SUB-AI-TEKNOFEST/DR_tiger.git
2. Install dependencies
  * python3 -m venv venv
  * . venv/bin/activate
  * pip3 install -r requirements.txt
3. Access data
  python3 untar.py
4. Run data_insert script to add data to the cloud or local (Change secret, host, graphname, username and password in the script).
 * python3 -m insert_data.data_insert
5. Steps to build/run project (Change secret, host, graphname, username and password in the script to use your own cloud account).
 * flask run or python3 app.py

## Known Issues and Future Improvements
* More data can be added to increase accuracy.
* The total project size can be reduced.

## Reflections
* tgcloud account was created.
* DRKG data loaded into the cloud database.
* model script was created.
* platform was created.
## References
Dataset: https://github.com/gnn4dr/DRKG
General TigerGraph and ML Knowledge https://medium.com/@karimsaraipour/gcn-with-tigergraph-and-pyg-a4ebff437d8a
