'''
Created on Mar 10, 2018

@author: ITAUser
'''
def tax(filing_status, income):
    if filing_status == 'single':
        if (income >= 0) and (income <= 9275):
            tax = (0.1*income)
        elif (income > 9275) and (income <= 37650):
            tax = (0.1*9275) + (0.15*(income - 9275))
        elif (income > 37650) and (income <= 91150):
            tax = (0.1*9275) + (0.15*(37650 - 9275)) + (0.25*(income - 37650))
        elif (income > 91150) and (income <= 190150):
            tax = (0.1*9275) + (0.15*(37650 - 9275)) + (0.25*(91150 - 37650)) + (0.28*(income - 91150))
        elif (income > 190150) and (income <= 413350):
             tax = (0.1*9275) + (0.15*(37650 - 9275)) + (0.25*(91150 - 37650)) + (0.28*(190150 - 91150)) + (0.33*(income - 190150))
        elif (income > 413350) and (income <= 415050):
             tax = (0.1*9275) + (0.15*(37650 - 9275)) + (0.25*(91150 - 37650)) + (0.28*(190150 - 91150)) + (0.33*(413350 - 190150)) + (0.35*(income - 413350))
        elif (income > 415050):
             tax = (0.1*9275) + (0.15*(37650 - 9275)) + (0.25*(91150 - 37650)) + (0.28*(190150 - 91150)) + (0.33*(413350 - 190150)) + (0.35*(415050 - 413350)) + (0.396*(income - 415050))
    elif filing_status == 'married filing jointly':
        if (income >= 0) and (income <= 18550):
            tax = (0.1*income)
        elif (income > 18550) and (income <= 75300):
             tax = (0.1*18550) + (0.15*(income - 18550))
        elif (income > 75300) and (income <= 151900):
             tax = (0.1*18500) + (0.15*(75300 - 18550)) + (0.25*(income - 75300))
        elif (income > 151900) and (income <= 231450):
             tax = (0.1*18550) + (0.15*(75300 - 18550)) + (0.25*(151900 - 75300)) + (0.28*(income - 151900))
        elif (income > 231450) and (income <= 413350):
             tax = (0.1*18550) + (0.15*(75300 - 18550)) + (0.25*(151900 - 75300)) + (0.28*(231450 - 151900)) + (0.33*(income - 231450))
        elif (income > 413350) and (income <= 466950):
             tax = (0.1*18550) + (0.15*(75300 - 18550)) + (0.25*(151900 - 75300)) + (0.28*(231450 - 151900)) + (0.33*(413350 - 231450)) + (0.35*(income - 413350))
        elif (income > 466950):
             tax = (0.1*18550) + (0.15*(75300 - 18550)) + (0.25*(151900 - 75300)) + (0.28*(231450 - 151900)) + (0.33*(413350 - 231450)) + (0.35*(466950 - 413350)) + (0.396*(income - 466950))
    elif filing_status == 'widow(er)':
        if (income >= 0) and (income <= 18550):
            tax = (0.1*income)
        elif (income > 18550) and (income <= 75300):
             tax = (0.1*18550) + (0.15*(income - 18550))
        elif (income > 75300) and (income <= 151900):
             tax = (0.1*18500) + (0.15*(75300 - 18550)) + (0.25*(income - 75300))
        elif (income > 151900) and (income <= 231450):
             tax = (0.1*18550) + (0.15*(75300 - 18550)) + (0.25*(151900 - 75300)) + (0.28*(income - 151900))
        elif (income > 231450) and (income <= 413350):
             tax = (0.1*18550) + (0.15*(75300 - 18550)) + (0.25*(151900 - 75300)) + (0.28*(231450 - 151900)) + (0.33*(income - 231450))
        elif (income > 413350) and (income <= 466950):
             tax = (0.1*18550) + (0.15*(75300 - 18550)) + (0.25*(151900 - 75300)) + (0.28*(231450 - 151900)) + (0.33*(413350 - 231450)) + (0.35*(income - 413350))
        elif (income > 466950):
             tax = (0.1*18550) + (0.15*(75300 - 18550)) + (0.25*(151900 - 75300)) + (0.28*(231450 - 151900)) + (0.33*(413350 - 231450)) + (0.35*(466950 - 413350)) + (0.396*(income - 466950))
    elif filing_status == 'married filing separately':
        if (income >= 0) and (income <= 9275):
            tax = (0.1*income)
        elif (income > 9275) and (income <= 37650):
            tax = (0.1*9275) + (0.15*(income - 9275))
        elif (income > 37650) and (income <= 75950):
            tax = (0.1*9275) + (0.15*(37650 - 9275)) + (0.25*(income - 37650))
        elif (income > 75950) and (income <= 115725):
            tax = (0.1*9275) + (0.15*(37650 - 9275)) + (0.25*(75950 - 37650)) + (0.28*(income - 75950))
        elif (income > 115725) and (income <= 206675):
             tax = (0.1*9275) + (0.15*(37650 - 9275)) + (0.25*(75950 - 37650)) + (0.28*(115725 - 75950)) + (0.33*(income - 115725))
        elif (income > 206675) and (income <= 233475):
             tax = (0.1*9275) + (0.15*(37650 - 9275)) + (0.25*(75950 - 37650)) + (0.28*(115725 - 75950)) + (0.33*(206675 - 115725)) + (0.35*(income - 206675))
        elif (income > 233475):
             tax = (0.1*9275) + (0.15*(37650 - 9275)) + (0.25*(75950 - 37650)) + (0.28*(115725 - 75950)) + (0.33*(206675 - 115725)) + (0.35*(233475 - 206675)) + (0.396*(income - 233475))
    elif filing_status == 'head of household':
        if (income >= 0) and (income <= 13250):
            tax = (0.1*income)
        elif (income > 13250) and (income <= 50400):
            tax = (0.1*13250) + (0.15*(income - 13250))
        elif (income > 50400) and (income <= 130150):
            tax = (0.1*13250) + (0.15*(50400 - 13250)) + (0.25*(income - 50400))
        elif (income > 130150) and (income <= 210800):
            tax = (0.1*13250) + (0.15*(50400 - 13250)) + (0.25*(130150 - 50400)) + (0.28*(income - 130150))
        elif (income > 210800) and (income <= 413350):
             tax = (0.1*13250) + (0.15*(50400 - 13250)) + (0.25*(130150 - 50400)) + (0.28*(210800 - 130150)) + (0.33*(income - 210800))
        elif (income > 413350) and (income <= 441000):
             tax = (0.1*13250) + (0.15*(50400 - 13250)) + (0.25*(130150 - 50400)) + (0.28*(210800 - 130150)) + (0.33*(413350 - 210800)) + (0.35*(income - 413350))
        elif (income > 441000):
             tax = (0.1*13250) + (0.15*(50400 - 13250)) + (0.25*(130150 - 50400)) + (0.28*(210800 - 130150)) + (0.33*(413350 - 210800)) + (0.35*(441000 - 413350)) + (0.396*(income - 441000))
    return tax
def percentage_of_tax(tax, income):
    return ((tax/income)*100)
def is_valid(filing_status, income):
    if (income < 0):
        return False
    elif (filing_status != 'single') and (filing_status != 'married filing jointly') and (filing_status != 'widow(er)') and (filing_status != 'married filing separately') and (filing_status != 'head of household'):
        return False
    return True
def main():
    filing_status = input("What is your filing Status? ")
    income = (int)(input("What is your income? "))
    if(is_valid(filing_status, income)):
        print(tax(filing_status, income))
    
main()
    
    
    