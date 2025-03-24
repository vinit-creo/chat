from dotenv import load_dotenv
from anthropic import Anthropic
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
SYSTEM_ROLE = os.getenv("SYSTEM_ENV")
BLUE = "\033[94m"
GREEN = "\033[92m"
RESET = "\033[0m"

anthropic = Anthropic(api_key=API_KEY,)


denial_letter= """Empire State Health Insurance 
275 Madison Avenue, Suite 1500 
New York, NY 10016 
Tel: (212) 555-8700 
 
Date: March 13, 2025 
Member Name: John Doe 
 Member ID: ESH78923456 
 Group Number: NY58721 
 Claim Number: CL-2025031254 
 Date of Service: February 22, 2025 
 Provider: Manhattan Medical Associates 
 
Dear John Doe, 
RE: NOTICE OF CLAIM DENIAL 
We have received and reviewed the claim submitted for services provided to you on February 
22, 2025, by Manhattan Medical Associates. After careful consideration, we regret to inform you 
that your claim has been denied for the following reason(s): 
Reason for Denial: The service(s) provided are not covered benefits under your current health 
plan. Specifically, the procedure code J9285 falls under experimental/investigational treatments, 
which are excluded from coverage as outlined in your Member Handbook, Section 4.3. 
Policy Reference: Your benefit plan specifically excludes "procedures, treatments, medications, 
or devices that are considered experimental or investigational by the Plan's Medical Review 
Board." (Member Handbook, page 27) 
What This Means: The full cost of $1,875.00 for this service will be your responsibility, unless 
this decision is overturned through the appeal process. 
Your Right to Appeal: You have the right to appeal this decision within 180 days from the date 
of this notice. Your appeal should include: 
●  A written statement explaining why you believe the claim should be covered 
●  Any additional documentation from your healthcare provider supporting medical 
necessity 
●  A copy of this denial letter 
How to Submit an Appeal: 
●  Online: www.empirestatehealth.com/appeals (login required) 
●  Mail: Empire State Health Insurance Appeals Department P.O. Box 9823 New York, NY 
10116 
●  Fax: (212) 555-8701 
If you need assistance with the appeals process, please contact our Member Services 
department at (800) 555-7290, Monday through Friday, 8:00 AM to 6:00 PM EST. 
External Review Rights: If your appeal is denied, you have the right to request an external 
review through the New York State Department of Financial Services within four months of 
receiving our final appeal determination. 
We understand that claim denials can be frustrating. Our Member Services representatives are 
available to discuss this determination and your coverage options in more detail. 
Sincerely, 
Amanda Rodriguez 
 Claims Review Specialist 
 Empire State Health Insurance 
 
This determination was made based on the terms of your benefit plan and our medical policies 
in effect at the time services were rendered. This letter serves as notice of your appeal rights 
under both your benefit plan and applicable state and federal laws. 
IMPORTANT NOTICE: The New York State Consumer Assistance Program (CAP) can help you 
file an appeal. Contact the CAP at 1-888-614-5400 or www.nyshealthconsumer.org for free 
assistance. 
 """



insurance_policy = """   EMPIRE STATE HEALTH INSURANCE
   COMPREHENSIVE HEALTH INSURANCE POLICY

**Policy Number:** ESHI-2025-10472893  
**Effective Date:** April 1, 2025  
**Policyholder:** John Doe

---

   POLICY OVERVIEW

This policy is a legal contract between Empire State Health Insurance ("Company," "we," "us," or "our") and the Policyholder ("you" or "your"). This policy provides benefits for covered medical services subject to the terms, conditions, limitations, and exclusions described herein.

---

   SECTION 1: DEFINITIONS

**Allowed Amount:** The maximum amount we will pay for a covered service.

**Coinsurance:** Your share of the costs of a covered health care service, calculated as a percentage of the allowed amount.

**Copayment:** A fixed amount you pay for a covered health care service.

**Deductible:** The amount you must pay for covered services before the insurance begins to pay.

**Emergency Services:** Medical services needed to evaluate or stabilize an emergency medical condition.

**Network Provider:** A provider who has contracted with us to provide services at negotiated rates.

**Out-of-Network Provider:** A provider who has not contracted with us.

**Premium:** The amount paid for health insurance coverage.

**Prior Authorization:** Approval from us before certain services are provided.

---

   SECTION 2: ELIGIBILITY AND ENROLLMENT

     2.1 Eligibility
To be eligible for coverage under this policy, you must:
- Be a resident of New York State
- Not be eligible for or enrolled in Medicare
- Meet all other eligibility requirements as specified in your application

     2.2 Dependent Eligibility
Eligible dependents include:
- Your legal spouse
- Your children under age 26
- Disabled dependents over age 26 who meet certain requirements

     2.3 Enrollment Period
- Initial Enrollment Period: Within 30 days of becoming eligible
- Annual Open Enrollment Period: November 1 - January 15
- Special Enrollment Period: Within 60 days of a qualifying life event

---

   SECTION 3: PREMIUM PAYMENT

     3.1 Premium Due Date
Premiums are due on the first day of each month.

     3.2 Grace Period
A grace period of 30 days is allowed for the payment of each premium after the first premium.

     3.3 Premium Changes
We may change premium rates upon 30 days written notice prior to the policy renewal date.

---

   SECTION 4: MEDICAL BENEFITS

     4.1 Deductible
- Individual Deductible: $1,500 per calendar year
- Family Deductible: $3,000 per calendar year

     4.2 Coinsurance
After the deductible is met, the plan pays 80  of covered charges for in-network services and 60  for out-of-network services.

     4.3 Out-of-Pocket Maximum
- Individual: $8,500 per calendar year (in-network)
- Family: $17,000 per calendar year (in-network)
- Out-of-network charges may exceed these limits

     4.4 Covered Services

| Service | In-Network | Out-of-Network |
|---------|------------|----------------|
| **Preventive Care** | 100  covered, no deductible | 60  after deductible |
| **Primary Care Visit** | $25 copay | 60  after deductible |
| **Specialist Visit** | $50 copay | 60  after deductible |
| **Urgent Care** | $75 copay | $75 copay |
| **Emergency Room** | $300 copay (waived if admitted) | $300 copay (waived if admitted) |
| **Inpatient Hospital** | 80  after deductible | 60  after deductible |
| **Outpatient Surgery** | 80  after deductible | 60  after deductible |
| **Laboratory Services** | 80  after deductible | 60  after deductible |
| **X-ray/Diagnostic Imaging** | 80  after deductible | 60  after deductible |
| **Advanced Imaging (CT/MRI)** | 80  after deductible | 60  after deductible |
| **Maternity Care** | 80  after deductible | 60  after deductible |
| **Mental Health/Substance Abuse (Outpatient)** | $25 copay | 60  after deductible |
| **Mental Health/Substance Abuse (Inpatient)** | 80  after deductible | 60  after deductible |
| **Rehabilitation Services** | 80  after deductible (60 visits/year) | 60  after deductible (60 visits/year) |
| **Durable Medical Equipment** | 80  after deductible | 60  after deductible |
| **Home Health Care** | 80  after deductible (40 visits/year) | 60  after deductible (40 visits/year) |
| **Skilled Nursing Facility** | 80  after deductible (60 days/year) | 60  after deductible (60 days/year) |
| **Hospice** | 80  after deductible (210 days/lifetime) | 60  after deductible (210 days/lifetime) |

---

   SECTION 5: PRESCRIPTION DRUG BENEFITS

     5.1 Prescription Drug Deductible
$200 individual / $400 family (does not apply to Tier 1 drugs)

     5.2 Prescription Drug Copays/Coinsurance (30-day supply)

| Tier | Retail Pharmacy | Mail Order (90-day supply) |
|------|----------------|---------------------------|
| **Tier 1 (Generic)** | $10 copay | $20 copay |
| **Tier 2 (Preferred Brand)** | $45 copay | $90 copay |
| **Tier 3 (Non-Preferred Brand)** | $90 copay | $180 copay |
| **Tier 4 (Specialty)** | 30  coinsurance (up to $250) | Not available |

     5.3 Formulary
The covered drugs are listed in the Empire State Health Insurance Formulary, which may be updated periodically.

---

   SECTION 6: EXCLUSIONS AND LIMITATIONS

This policy does not cover:
1. Services not medically necessary
2. Experimental or investigational treatments
3. Cosmetic procedures (unless medically necessary)
4. Dental care (except as specifically provided)
5. Vision care (except as specifically provided)
6. Long-term care
7. Non-emergency care when traveling outside the U.S.
8. Private-duty nursing
9. Weight loss programs
10. Services covered by workers' compensation
11. Services received without required prior authorization
12. Charges exceeding the allowed amount

---

   SECTION 7: CLAIM PROCEDURES

     7.1 Filing Claims
Network providers will file claims directly with us. For services from out-of-network providers, you must submit a claim form within 120 days of service.

     7.2 Claim Determination
We will make a determination on claims within:
- 30 days for standard claims
- 72 hours for urgent claims

     7.3 Appeals
If you disagree with a claim determination, you may file an appeal within 180 days of receiving notice of the determination.

---

   SECTION 8: COORDINATION OF BENEFITS

If you are covered under more than one health plan, benefits will be coordinated with other plans according to state regulations.

---

   SECTION 9: TERMINATION OF COVERAGE

     9.1 Termination by Policyholder
You may terminate this policy at any time with written notice.

     9.2 Termination by Company
We may terminate this policy for:
- Nonpayment of premiums
- Fraud or intentional misrepresentation
- Policyholder no longer residing in the service area
- Discontinuation of this type of coverage

     9.3 Continuation of Coverage
You may be eligible for continuation of coverage under COBRA or New York State continuation provisions.

---

   SECTION 10: GENERAL PROVISIONS

     10.1 Entire Contract
This policy, including the application and any amendments, constitutes the entire contract.

     10.2 Time Limit on Certain Defenses
After two years from the policy effective date, no misstatements made by the policyholder shall be used to void the policy.

     10.3 Changes to Policy
No change to this policy is valid unless approved by an executive officer of the Company.

     10.4 Legal Actions
No legal action may be brought against us until 60 days after written proof of loss has been given or more than three years after the time written proof of loss is required.

     10.5 Conformity with State Statutes
Any provision of this policy that conflicts with state law is amended to conform to minimum requirements.

---

   CONTACT INFORMATION

**Customer Service:** 1-800-555-ESHI (3744)  
**Website:** www.empirestatehealth.com  
**Email:** customerservice@empirestatehealth.com  
**Address:** Empire State Health Insurance, 123 Healthcare Plaza, Albany, NY 12205

---

*This document is a sample policy and does not constitute an actual insurance contract. Terms, conditions, and rates may vary based on individual circumstances and underwriting decisions.*"""

def chat():
    conversation = []

       
    print(f"{GREEN}Claude: {RESET}", end="", flush=True)
    value = anthropic.messages.create(system=SYSTEM_ROLE, 
                         messages=[
            {"role": "user", "content": f"Generate summary of the points with which I can appeal to the denial letter by an health insurance company as text here {denial_letter} as per the policy document {insurance_policy}. Do not assume anything, use the facts that are as present in the two inputs. Basically generate a few bullet points to include in my appeal letter, along with that based on the two inputs here do let me know the probability of my appeakls claims to be reconsidered."}
        ],
                                  max_tokens=500,
                                  model="claude-3-haiku-20240307",
                                  stream=True,
                                  temperature=1,)
    assistance_response = ""
    for chunk in value:
         if chunk.type == "content_block_delta":
            content = chunk.delta.text
            print(f"{GREEN}{content}{RESET}", end="", flush=True)
            assistance_response != content



def processDocument():
     # TODO: add code to process a PRf file of  the denial letter here get it form https://github.com/fighthealthinsurance/fighthealthinsurance.git
    print()



if __name__ =="__main__":
    chat()


