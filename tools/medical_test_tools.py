# Medical test tools for healthcare agents
# Provides simulated medical test functionality

import random
from agno.tools import Toolkit


class MedicalTestTools(Toolkit):
    """Medical test tools for simulating diagnostic tests and returning random outcomes."""

    def __init__(self, **kwargs):
        tools = [
            self.cbc,
            self.bmp,
            self.cmp,
            self.urinalysis,
            self.liver_function_tests,
            self.thyroid_function_tests,
            self.lipid_panel,
            self.hemoglobin_a1c,
            self.prothrombin_time,
            self.ptt,
            self.crp,
            self.esr,
            self.blood_cultures,
            self.stool_culture,
            self.chest_xray,
            self.ecg,
            self.echocardiogram,
            self.pulmonary_function_tests,
            self.ct_scan,
            self.mri_scan,
            self.ultrasound,
            self.mammogram,
            self.pap_smear,
            self.colonoscopy,
            self.endoscopy,
            self.bone_density_scan,
            self.allergy_testing,
            self.hiv_test,
            self.hepatitis_panel,
            self.rheumatoid_factor,
            self.ana_test,
            self.d_dimer,
            self.troponin,
            self.blood_gas_analysis,
            self.sputum_culture,
            self.genetic_testing,
            self.vitamin_d_level,
            self.ferritin,
            self.testosterone_level,
            self.psa,
            self.pregnancy_test,
            self.rapid_strep_test,
        ]
        super().__init__(name="medical_test_tools", tools=tools, **kwargs)

    def cbc(self) -> str:
        """Complete Blood Count (CBC)
        
        Measures the levels of different cells in the blood, such as red blood cells, white blood cells, and platelets.
        """
        outcomes = ["Normal", "Anemia", "Leukocytosis", "Leukopenia", "Thrombocytopenia", "Polycythemia"]
        return random.choice(outcomes)

    def bmp(self) -> str:
        """Basic Metabolic Panel (BMP)
        
        Evaluates kidney function, blood sugar levels, and electrolyte balance.
        """
        outcomes = ["Normal", "Electrolyte Imbalance", "Renal Dysfunction", "Hyperglycemia", "Hypoglycemia"]
        return random.choice(outcomes)

    def cmp(self) -> str:
        """Comprehensive Metabolic Panel (CMP)
        
        Provides information about the liver, kidneys, and electrolyte and acid/base balance, as well as blood sugar and proteins.
        """
        outcomes = ["Normal", "Liver Dysfunction", "Renal Dysfunction", "Electrolyte Imbalance", "Hyperglycemia", "Hypoglycemia"]
        return random.choice(outcomes)

    def urinalysis(self) -> str:
        """Urinalysis
        
        Analyzes urine to detect and manage a wide range of disorders, such as urinary tract infections, kidney disease, and diabetes.
        """
        outcomes = ["Normal", "Urinary Tract Infection", "Hematuria", "Proteinuria", "Glucosuria"]
        return random.choice(outcomes)

    def liver_function_tests(self) -> str:
        """Liver Function Tests
        
        Measures enzymes, proteins, and substances produced or excreted by the liver to assess its health.
        """
        outcomes = ["Normal", "Elevated Liver Enzymes", "Hepatitis", "Cirrhosis"]
        return random.choice(outcomes)

    def thyroid_function_tests(self) -> str:
        """Thyroid Function Tests
        
        Evaluates the function of the thyroid gland by measuring levels of thyroid hormones in the blood.
        """
        outcomes = ["Normal", "Hypothyroidism", "Hyperthyroidism"]
        return random.choice(outcomes)

    def lipid_panel(self) -> str:
        """Lipid Panel
        
        Measures cholesterol and triglycerides in the blood to assess cardiovascular health.
        """
        outcomes = ["Normal", "Hyperlipidemia", "Low HDL", "High LDL", "High Triglycerides"]
        return random.choice(outcomes)

    def hemoglobin_a1c(self) -> str:
        """Hemoglobin A1c
        
        Measures average blood sugar levels over the past 2-3 months to diagnose and monitor diabetes.
        """
        outcomes = ["Normal", "Prediabetes", "Diabetes"]
        return random.choice(outcomes)

    def prothrombin_time(self) -> str:
        """Prothrombin Time (PT)/INR
        
        Measures how long it takes blood to clot to assess bleeding or clotting disorders.
        """
        outcomes = ["Normal", "Prolonged PT/INR", "Risk of Bleeding"]
        return random.choice(outcomes)

    def ptt(self) -> str:
        """Partial Thromboplastin Time (PTT)
        
        Evaluates the blood's ability to clot by measuring the time it takes for a clot to form.
        """
        outcomes = ["Normal", "Prolonged PTT", "Risk of Bleeding"]
        return random.choice(outcomes)

    def crp(self) -> str:
        """C-Reactive Protein (CRP)
        
        Measures the level of C-reactive protein in the blood to detect inflammation.
        """
        outcomes = ["Normal", "Elevated CRP (Inflammation)"]
        return random.choice(outcomes)

    def esr(self) -> str:
        """Erythrocyte Sedimentation Rate (ESR)
        
        Measures the rate at which red blood cells settle at the bottom of a test tube, indicating inflammation.
        """
        outcomes = ["Normal", "Elevated ESR (Inflammation)"]
        return random.choice(outcomes)

    def blood_cultures(self) -> str:
        """Blood Cultures
        
        Detects the presence of bacteria or fungi in the blood to diagnose infections.
        """
        outcomes = ["No Growth", "Bacterial Infection", "Fungal Infection"]
        return random.choice(outcomes)

    def stool_culture(self) -> str:
        """Stool Culture
        
        Identifies pathogens in the stool to diagnose gastrointestinal infections.
        """
        outcomes = ["No Pathogen", "Bacterial Infection", "Parasitic Infection"]
        return random.choice(outcomes)

    def chest_xray(self) -> str:
        """Chest X-ray
        
        Imaging test that uses X-rays to view the lungs and heart.
        """
        outcomes = ["Normal", "Pneumonia", "Pleural Effusion", "Mass", "Fracture"]
        return random.choice(outcomes)

    def ecg(self) -> str:
        """Electrocardiogram (ECG/EKG)
        
        Records the electrical activity of the heart to identify heart problems.
        """
        outcomes = ["Normal", "Arrhythmia", "Myocardial Infarction", "Ischemia"]
        return random.choice(outcomes)

    def echocardiogram(self) -> str:
        """Echocardiogram
        
        Uses ultrasound waves to create images of the heart's structure and function.
        """
        outcomes = ["Normal", "Valve Disease", "Heart Failure", "Cardiomyopathy"]
        return random.choice(outcomes)

    def pulmonary_function_tests(self) -> str:
        """Pulmonary Function Tests
        
        Measures how well the lungs are working, including the amount of air inhaled, exhaled, and the speed of the air.
        """
        outcomes = ["Normal", "Obstructive Pattern", "Restrictive Pattern"]
        return random.choice(outcomes)

    def ct_scan(self, scan_type: str = "general") -> str:
        """CT Scan
        
        Imaging test that uses X-rays and computer technology to see inside the body.
        
        Args:
            scan_type: Type of CT scan (e.g., 'general', 'chest', 'abdominal', 'head', 'ct_pulmonary_angiography', 'cardiac')
        """
        # Different outcomes based on scan type
        if "pulmonary" in scan_type.lower() or "chest" in scan_type.lower():
            outcomes = ["Normal", "Pulmonary embolism", "Pneumonia", "Mass", "Pleural effusion", "Pneumothorax"]
        elif "cardiac" in scan_type.lower() or "heart" in scan_type.lower():
            outcomes = ["Normal", "Coronary calcification", "Aortic aneurysm", "Pericardial effusion"]
        elif "head" in scan_type.lower() or "brain" in scan_type.lower():
            outcomes = ["Normal", "Hemorrhage", "Mass", "Stroke", "Hydrocephalus"]
        elif "abdominal" in scan_type.lower() or "abdomen" in scan_type.lower():
            outcomes = ["Normal", "Mass", "Obstruction", "Inflammation", "Fluid collection"]
        else:
            # General CT scan outcomes
            outcomes = ["Normal", "Mass", "Hemorrhage", "Fracture", "Infection"]
        
        result = random.choice(outcomes)
        return f"CT Scan ({scan_type}): {result}"

    def mri_scan(self, scan_type: str = "general") -> str:
        """MRI Scan
        
        Uses magnetic fields and radio waves to create detailed images of organs and tissues inside the body.
        
        Args:
            scan_type: Type of MRI scan (e.g., 'general', 'brain', 'spine', 'cardiac', 'abdominal')
        """
        if "brain" in scan_type.lower() or "head" in scan_type.lower():
            outcomes = ["Normal", "Mass", "Lesion", "Stroke", "Multiple sclerosis", "Hemorrhage"]
        elif "spine" in scan_type.lower():
            outcomes = ["Normal", "Disc herniation", "Stenosis", "Compression fracture", "Tumor"]
        elif "cardiac" in scan_type.lower() or "heart" in scan_type.lower():
            outcomes = ["Normal", "Cardiomyopathy", "Wall motion abnormality", "Valve dysfunction"]
        elif "abdominal" in scan_type.lower():
            outcomes = ["Normal", "Mass", "Organ enlargement", "Fluid collection", "Inflammation"]
        else:
            # General MRI outcomes
            outcomes = ["Normal", "Mass", "Lesion", "Stroke", "Degeneration"]
        
        result = random.choice(outcomes)
        return f"MRI Scan ({scan_type}): {result}"

    def ultrasound(self, scan_type: str = "general") -> str:
        """Ultrasound
        
        Uses high-frequency sound waves to create images of the inside of the body.
        
        Args:
            scan_type: Type of ultrasound (e.g., 'general', 'abdominal', 'cardiac', 'pelvic', 'pregnancy', 'vascular')
        """
        if "cardiac" in scan_type.lower() or "echo" in scan_type.lower():
            outcomes = ["Normal", "Valve dysfunction", "Wall motion abnormality", "Cardiomyopathy", "Pericardial effusion"]
        elif "abdominal" in scan_type.lower():
            outcomes = ["Normal", "Gallstones", "Kidney stones", "Liver mass", "Fluid collection"]
        elif "pelvic" in scan_type.lower():
            outcomes = ["Normal", "Ovarian cyst", "Uterine fibroid", "Endometrial thickening"]
        elif "pregnancy" in scan_type.lower() or "obstetric" in scan_type.lower():
            outcomes = ["Normal fetal development", "Multiple pregnancy", "Growth restriction", "Placental abnormality"]
        elif "vascular" in scan_type.lower():
            outcomes = ["Normal", "Deep vein thrombosis", "Arterial stenosis", "Aneurysm"]
        else:
            # General ultrasound outcomes
            outcomes = ["Normal", "Cyst", "Mass", "Gallstones", "Pregnancy"]
        
        result = random.choice(outcomes)
        return f"Ultrasound ({scan_type}): {result}"

    def mammogram(self) -> str:
        """Mammogram
        
        X-ray of the breast used to detect tumors or abnormalities.
        """
        outcomes = ["Normal", "Benign Mass", "Suspicious Mass", "Calcifications"]
        return random.choice(outcomes)

    def pap_smear(self) -> str:
        """Pap Smear
        
        Screens for cervical cancer in women by collecting cells from the cervix.
        """
        outcomes = ["Normal", "Low-grade Lesion", "High-grade Lesion", "Cancer"]
        return random.choice(outcomes)

    def colonoscopy(self) -> str:
        """Colonoscopy
        
        Examines the colon and rectum for abnormalities or disease by inserting a flexible tube with a camera.
        """
        outcomes = ["Normal", "Polyp", "Cancer", "Inflammation"]
        return random.choice(outcomes)

    def endoscopy(self) -> str:
        """Endoscopy
        
        Examines the digestive tract using a flexible tube with a light and camera.
        """
        outcomes = ["Normal", "Ulcer", "Polyp", "Cancer", "Inflammation"]
        return random.choice(outcomes)

    def bone_density_scan(self) -> str:
        """Bone Density Scan
        
        Measures the density of minerals (such as calcium) in bones to assess bone health.
        """
        outcomes = ["Normal", "Osteopenia", "Osteoporosis"]
        return random.choice(outcomes)

    def allergy_testing(self) -> str:
        """Allergy Testing
        
        Identifies specific allergens that may be causing allergic reactions.
        """
        outcomes = ["No Allergy", "Allergic Reaction"]
        return random.choice(outcomes)

    def hiv_test(self) -> str:
        """HIV Test
        
        Detects the presence of antibodies to the HIV virus in the blood.
        """
        outcomes = ["Negative", "Positive"]
        return random.choice(outcomes)

    def hepatitis_panel(self) -> str:
        """Hepatitis Panel
        
        Detects the presence of hepatitis viruses in the blood.
        """
        outcomes = ["Negative", "Positive for Hepatitis A", "Positive for Hepatitis B", "Positive for Hepatitis C"]
        return random.choice(outcomes)

    def rheumatoid_factor(self) -> str:
        """Rheumatoid Factor
        
        Detects the presence of rheumatoid factor antibodies in the blood, which may indicate rheumatoid arthritis.
        """
        outcomes = ["Negative", "Positive"]
        return random.choice(outcomes)

    def ana_test(self) -> str:
        """ANA (Antinuclear Antibody Test)
        
        Detects antinuclear antibodies in the blood that may indicate an autoimmune disorder.
        """
        outcomes = ["Negative", "Positive"]
        return random.choice(outcomes)

    def d_dimer(self) -> str:
        """D-dimer
        
        Measures the level of D-dimer in the blood, which may indicate the presence of an abnormal blood clot.
        """
        outcomes = ["Normal", "Elevated (Possible Clot)"]
        return random.choice(outcomes)

    def troponin(self) -> str:
        """Troponin
        
        Measures the level of troponin in the blood, which may indicate heart muscle damage.
        """
        outcomes = ["Normal", "Elevated (Possible MI)"]
        return random.choice(outcomes)

    def blood_gas_analysis(self) -> str:
        """Blood Gas Analysis
        
        Measures the levels of oxygen and carbon dioxide in the blood, as well as the blood's pH.
        """
        outcomes = ["Normal", "Acidosis", "Alkalosis", "Hypoxemia"]
        return random.choice(outcomes)

    def sputum_culture(self) -> str:
        """Sputum Culture
        
        Identifies pathogens in the sputum (mucus from the respiratory tract) to diagnose respiratory infections.
        """
        outcomes = ["No Pathogen", "Bacterial Infection", "Fungal Infection"]
        return random.choice(outcomes)

    def genetic_testing(self) -> str:
        """Genetic Testing
        
        Analyzes DNA to identify genetic mutations or variations that may be associated with certain diseases or conditions.
        """
        outcomes = ["No Mutation", "Pathogenic Mutation", "Variant of Unknown Significance"]
        return random.choice(outcomes)

    def vitamin_d_level(self) -> str:
        """Vitamin D Level
        
        Measures the level of vitamin D in the blood to assess vitamin D deficiency or insufficiency.
        """
        outcomes = ["Normal", "Deficiency", "Insufficiency"]
        return random.choice(outcomes)

    def ferritin(self) -> str:
        """Ferritin
        
        Measures the level of ferritin in the blood, which reflects the amount of stored iron in the body.
        """
        outcomes = ["Normal", "Low (Iron Deficiency)", "High (Iron Overload)"]
        return random.choice(outcomes)

    def testosterone_level(self) -> str:
        """Testosterone Level
        
        Measures the level of testosterone in the blood to assess hormonal balance.
        """
        outcomes = ["Normal", "Low", "High"]
        return random.choice(outcomes)

    def psa(self) -> str:
        """PSA (Prostate-Specific Antigen)
        
        Measures the level of PSA in the blood, which may be elevated in prostate cancer or benign prostatic hyperplasia.
        """
        outcomes = ["Normal", "Elevated (Possible Cancer)", "Benign Prostatic Hyperplasia"]
        return random.choice(outcomes)

    def pregnancy_test(self) -> str:
        """Pregnancy Test
        
        Detects the presence of the hormone hCG in the blood or urine, indicating pregnancy.
        """
        outcomes = ["Negative", "Positive"]
        return random.choice(outcomes)

    def rapid_strep_test(self) -> str:
        """Rapid Strep Test
        
        Detects streptococcal bacteria in the throat to diagnose strep throat.
        """
        outcomes = ["Negative", "Positive"]
        return random.choice(outcomes)
