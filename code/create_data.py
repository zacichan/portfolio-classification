import pandas as pd
import random

# Seed for reproducibility
random.seed(42)

# Existing research descriptions
descriptions = [
    "Study on the effects of various pollutants on marine biology and ecosystem health.",
    "Development of machine learning algorithms for financial market predictions.",
    "Research on the genetic modification of crops to improve resistance to pests.",
    "Analysis of the impact of social media on mental health among teenagers.",
    "Investigation into the role of gut microbiota in human digestion and health.",
    "Evaluation of renewable energy sources and their potential for reducing carbon emissions.",
    "Study on the behavioral patterns of primates in different environmental conditions.",
    "Development of blockchain technology applications for secure online transactions.",
    "Research on the photosynthetic efficiency of different plant species under varying light conditions.",
    "Assessment of urban planning strategies to mitigate traffic congestion in large cities.",
]

# Additional descriptions for protein synthesis research
protein_synthesis_descriptions = [
    "Investigation of ribosomal activity during protein synthesis.",
    "Study on the effects of antibiotics on protein synthesis in bacteria.",
    "Research on the role of tRNA in the translation process of protein synthesis.",
    "Analysis of protein folding mechanisms and their impact on cellular functions.",
    "Study on the regulation of gene expression during protein synthesis.",
    "Evaluation of post-translational modifications in protein synthesis.",
    "Investigation into the role of chaperone proteins in protein synthesis.",
    "Research on the effects of genetic mutations on protein synthesis efficiency.",
    "Study on the synthesis of membrane proteins and their cellular transport.",
    "Analysis of the impact of environmental stressors on protein synthesis in plants.",
]

# Generate additional non-protein synthesis research descriptions
additional_descriptions = [
    "Study on the migration patterns of birds in relation to climate change.",
    "Research on the development of new materials for use in solar cells.",
    "Investigation into the effects of microplastics on freshwater ecosystems.",
    "Analysis of the economic impact of automation on manufacturing industries.",
    "Study on the effectiveness of various cancer treatment therapies.",
    "Research on the use of AI in early disease detection and diagnostics.",
    "Evaluation of the impact of diet and nutrition on cardiovascular health.",
    "Investigation into the genetic basis of inherited neurological disorders.",
    "Analysis of the role of biodiversity in maintaining ecosystem stability.",
    "Study on the development of vaccines for emerging infectious diseases.",
    "Research on the long-term effects of space travel on human physiology.",
    "Evaluation of the use of drones in precision agriculture.",
    "Investigation into the psychological effects of virtual reality experiences.",
    "Study on the impact of urban green spaces on public health.",
    "Research on the development of biodegradable plastics.",
    "Analysis of the efficiency of different waste management practices.",
    "Study on the role of epigenetics in cancer development and progression.",
    "Research on the impact of air pollution on respiratory health.",
    "Investigation into the potential of gene therapy for treating genetic disorders.",
    "Analysis of the effects of climate change on agricultural productivity.",
    "Study on the application of CRISPR technology in genetic engineering.",
    "Research on the development of renewable biofuels.",
    "Evaluation of the role of education in social mobility.",
    "Investigation into the impact of deforestation on local climates.",
    "Analysis of the role of technology in modern education.",
    "Study on the effectiveness of mindfulness practices in stress reduction.",
    "Research on the impact of global trade policies on developing economies.",
    "Investigation into the relationship between exercise and mental health.",
    "Analysis of the potential benefits of vertical farming in urban areas.",
    "Study on the development of new drug delivery systems.",
    "Research on the effects of sleep deprivation on cognitive function.",
    "Evaluation of the sustainability of different fishing practices.",
    "Investigation into the potential of quantum computing in solving complex problems.",
    "Analysis of the impact of artificial intelligence on job markets.",
    "Study on the role of nanotechnology in medical treatments.",
    "Research on the development of smart grid technology for energy distribution.",
    "Evaluation of the effects of noise pollution on wildlife.",
    "Investigation into the use of robotics in elderly care.",
    "Analysis of the impact of cultural heritage on community identity.",
    "Study on the development of antiviral drugs for combating pandemics.",
    "Research on the use of big data in climate modeling.",
    "Investigation into the effects of dietary supplements on athletic performance.",
    "Analysis of the role of microorganisms in soil health.",
    "Study on the development of advanced prosthetic limbs.",
    "Research on the impact of technology on traditional industries.",
    "Evaluation of the effectiveness of different teaching methods in STEM education.",
    "Investigation into the potential of renewable energy storage solutions.",
    "Analysis of the psychological effects of chronic pain.",
    "Study on the relationship between genetics and longevity.",
    "Research on the effects of urbanization on local wildlife.",
    "Evaluation of the impact of policy changes on public health outcomes.",
    "Investigation into the role of telemedicine in rural healthcare.",
    "Analysis of the effects of climate change on ocean currents.",
    "Study on the development of environmentally friendly pesticides.",
    "Research on the influence of social networks on political opinions.",
    "Evaluation of the benefits of early childhood education programs.",
    "Investigation into the potential of algae as a source of biofuel.",
    "Analysis of the impact of tourism on natural reserves.",
    "Study on the development of earthquake-resistant building materials.",
    "Research on the effects of aging on cognitive decline.",
    "Evaluation of the role of physical activity in preventing chronic diseases.",
    "Investigation into the genetic diversity of endangered species.",
    "Analysis of the impact of renewable energy adoption on economic growth.",
    "Study on the effectiveness of public health campaigns in disease prevention.",
    "Research on the development of new antibiotics to combat resistant bacteria.",
    "Evaluation of the potential of vertical wind turbines in urban settings.",
    "Investigation into the role of sleep in memory consolidation.",
    "Analysis of the effects of green roofs on building energy efficiency.",
    "Study on the development of advanced materials for aerospace applications.",
    "Research on the impact of dietary patterns on gut health.",
    "Evaluation of the potential of hydroponics for sustainable agriculture.",
    "Investigation into the effects of climate change on polar ice melt.",
    "Analysis of the role of artificial intelligence in healthcare diagnostics.",
    "Study on the impact of human activity on coral reef ecosystems.",
    "Research on the development of personalized medicine based on genetic profiling.",
    "Evaluation of the effects of urban sprawl on local ecosystems.",
    "Investigation into the potential of CRISPR-Cas9 in gene editing.",
    "Analysis of the impact of renewable energy subsidies on market dynamics.",
    "Study on the role of biomarkers in early disease detection.",
    "Research on the influence of climate change on migratory species.",
    "Evaluation of the effectiveness of immunotherapy in cancer treatment.",
    "Investigation into the relationship between air quality and respiratory diseases.",
]

# Combine the lists ensuring 10 are related to protein synthesis
all_descriptions = protein_synthesis_descriptions + additional_descriptions[:90]

# Shuffle the combined list to mix protein synthesis and other research topics
random.shuffle(all_descriptions)

# Create a DataFrame
df = pd.DataFrame(all_descriptions[:100], columns=["description"])

df.head()

# Save the DataFrame to a CSV file
df.to_csv('data/synthetic_data.csv', index=False)
