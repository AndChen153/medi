q=0
e=0
print ("Welcome to the Diseases Dictionary")
print ("1 - poor blood clotting \n \
       2 - exaggerated bleeding \n \
       3 - tiredness \n \
       4 - stomach discomfort \n \
       5 - fever \n \
       6 - decreased appetite \n \
       7 - diarrhea \n \
       8 - light-colored stools \n \
       9 - dark yellow urine \n \
       10 - jaundice \n \
       11 - chills \n \
       12 - headaches \n \
       13 - muscle aches \n \
       14 - cough \n \
       15 - congestion \n \
       16 - runny nose \n \
       17 - fatigue \n \
       18 - muscle pain\n \
       19 - burning pain in chest that occurs after eating and worsens when lying down\n \
       20 - sneezing \n \
       21 - swelling\n \
       22 - nausea\n \
       23 - skin rash\n \
       24 - inability to exercise\n \
       25 - loss of appetite\n \
       26 - low oxygen in the body\n \
       27 - sleepiness\n \
       28 - sleeping difficlty\n \
       29 - rapid breathing\n \
       30 - shortness of breath\n \
       31 - fast heart rate\n \
       32 - vomiting\n \
       33 - memory loss\n \
       34 - confusion\n \
       35 - behavioral issues\n \
       36 - differing from regular moods\n \
       37 - depression\n \
       38 - hallucinations\n \
       39 - paranoia\n \
       40 - inability to combine muscle movements\n \
       41 - jumbled speech")

diseases = {
    "hemophilia-coagulation factor replacement therapy" : ["1", "2"],
    "hepatitus a-hepatitus a vacine" : ["3","4","5","6","7","8","9","10"],
    "influenza-otc medications for decongestants, cough medicine, nosteroidal anti-inflamatory drug, analgesic, antiviral drug" : ["3","5","11","12","13","14","15","16","17","18", "20"],
    "acid reflux-antacid, proton-pump inhibitor, diarrhea medication, elevate head of bed, dietary modification, weight loss" : ["19"],
    "allergies-imunotherapy(see a docotor to find out what you are allegric to" : ["12","20","16","21","22","7","23"],
    "altitude sickness-pain medication, more extreme cases require oxygen and movingn to a lower altitude" : ["24","17","25","26","27","28","22","32","29","30","31","12"],
    "alzheimer/'s-no cure, but cognitive-enhancing medications and physical exercise can help" : ["33","34","35","36","37","38","39","40","41","25"],
    
    }
o=len(diseases)
o=o+10
while e<o:
    x=input ("what are your symptoms?")
    if x=='done':
        break
    for i in diseases:
        if x not in diseases[i]:
            diseases[i]='a'
    #print (diseases)
    e=e+1

if e<3:
    print ("You may want to input more symptoms for a more accurate diagnosis.")
print ('\nYou show the symptoms for these disease(s):')
for i in diseases:
    if 'a' not in diseases[i]:
        print (i)
        q=1
if q==0:
    print ('No disease with these symptoms in our database.')


        
    
