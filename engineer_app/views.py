from datetime import datetime
import math
from django.shortcuts import render, HttpResponse
from .models import TodoItem
# Create your views here.
def home(request):
    return render(request, "home.html")

def calculate(request):
    return render(request, "calculator.html")

def calculate2(request):
    return render(request, "calculator2.html")

def calculate3(request):
    return render(request, "calculator3.html")

def amound_anuality(request):
    return render(request, "calculator3/amound_anuality.html")

def capital_anuality(request):
    return render(request, "calculator3/capital_anuality.html")

def term_anuality(request):
    return render(request, "calculator3/rent_anuality.html")

def compound_amount(request):
    return render(request, "calculator2/compound_amount.html")

def compound_capital(request):
    return render(request, "calculator2/compound_capital.html")

def compound_tax_rate(request):
    return render(request, "calculator2/compound_tax_rate.html")

def compound_time(request):
    return render(request, "calculator2/compound_time.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todo.html", {"todos": items})

def future_value(request):
    return render(request, "calculator/future_value.html")

def tax_value(request):
    return render(request, "calculator/tax_value.html")

def capital_value(request):
    return render(request, "calculator/capital_value.html")

def tax_rate_value(request):
    return render(request, "calculator/tax_rate_value.html")

def time_value(request):
    return render(request, "calculator/time_value.html")

def load_page(request, page_name):
    return render(request, f'{page_name}.html')

def calculate_days(initialDay, initialMonth, initialYear, finalDay, finalMonth, finalYear):
    # Convertir las fechas iniciales y finales a objetos datetime
    initial_date = datetime(initialYear, initialMonth, initialDay)
    final_date = datetime(finalYear, finalMonth, finalDay)
    
    # Calcular la diferencia en días
    difference = final_date - initial_date
    difference_days = difference.days
    print("La diferencia en días es:", difference_days)
    
    return difference_days

# OK.
def calculate_future_value(request):
    if request.method == 'POST':
        try:
            # VP - Valor Presente
            presentValue = float(request.POST['value1'])
            # % de interes
            taxPercentage = float(request.POST['value2'])
            # fecha inicial ---------------
            # dia
            initialDay = int(request.POST['value3'])
            # mes
            initialMonth = int(request.POST['value4'])
            # año
            initialYear = int(request.POST['value5'])
            
            # fecha final ---------------
            # dia
            finalDay = int(request.POST['value6'])
            # mes
            finalMonth = int(request.POST['value7'])
            # año
            finalYear = int(request.POST['value8'])
            
            result = (presentValue)*(1+(taxPercentage/100)*(calculate_days(initialDay, initialMonth, initialYear, finalDay, finalMonth, finalYear)/365))
            result = round(result, 2)
            result = str(result) + " $"
        except Exception as e:
            result = "Ocurrió un error: " + str(e)
        return render(request, 'result.html', {'result': result})
    return render(request, 'calculator.html')
# OK.
def calculate_tax_value(request):
    if request.method == 'POST':
        try:
            # C - Capital 
            capitalValue = float(request.POST['value1'])
            # % de interes
            itPercentage = float(request.POST['value2'])
            # tiempo ---------------
            # año
            year = int(request.POST['value3'])
            # mes
            month = int(request.POST['value4'])
            # dia
            day = int(request.POST['value5'])
            
            result = capitalValue*(itPercentage/100)*(year+(month/12)+(day/365))
            result = round(result, 2)
            result = str(result) + " $"
        except Exception as e:
            result = "Ocurrió un error: " + str(e)
        return render(request, 'result.html', {'result': result})
    return render(request, 'calculator.html')

# OK.
def calculate_capital_value(request):
    if request.method == 'POST':
        try:
            # C - Inicial
            capitalValue = float(request.POST['value1'])
            # I - Interes 
            taxValue = float(request.POST['value2'])
            # % de interes
            itPercentage = float(request.POST['value3'])
            # tiempo ---------------
            # año
            year = int(request.POST['value4'])
            # mes
            month = int(request.POST['value5'])
            # dia
            day = int(request.POST['value6'])
            # para año
            toYear = ((month / 12 )+(day / 360))
            # Hallando resultado ----
            result = 0
            if (capitalValue == 0):
                result = taxValue/((itPercentage/100)*(year+toYear))
            else:
                ipt = (capitalValue * (year+toYear) * (itPercentage/100))
                result  = (capitalValue + itPercentage)+ipt
            result = round(result, 2)
            result = str(result) + " $"
        except Exception as e:
            result = "Ocurrió un error: " + str(e)
        return render(request, 'result.html', {'result': result})
    return render(request, 'calculator.html')
# OK.
def calculate_tax_rate_value(request):
    if request.method == 'POST':
        try:
            # I - Interes 
            taxValue = float(request.POST['value1'])
            # Capital inicial - CI
            capitalInitialValue = float(request.POST['value2'])
            # Capital final - CF
            capitalFinalValue = float(request.POST['value3'])
            # tiempo ---------------
            # año
            year = int(request.POST['value4'])
            # mes
            month = int(request.POST['value5'])
            # dia
            day = int(request.POST['value6'])
            
            result = 0
            if (capitalInitialValue != 0 and capitalFinalValue!= 0):
                # CUANDO NOS DAN CAPITAL INICIAL Y FINAL, PARA HALLAR TASA DE INTERES EN UN INTERVALO
                result = ((capitalFinalValue - capitalInitialValue)/(capitalInitialValue))*100
            else:
                result = (taxValue/((capitalInitialValue)*(year+(month/12)+(day/360))))*100
            result = round(result, 2)
            result = str(result) + " %"
        except Exception as e:
            result = "Ocurrió un error: " + str(e)
        return render(request, 'result.html', {'result': result})
    return render(request, 'calculator.html')

# OK.
def calculate_time_value(request):
    if request.method == 'POST':
        try:
            # I - Interes 
            taxValue = float(request.POST['value1'])
            # Capital inicial - CI
            capitalInitialValue = float(request.POST['value2'])
            # Capital final - CF
            capitalFinalValue = float(request.POST['value3'])
            # % tasa de interes
            taxRateValue = float(request.POST['value4'])
            # % tasa de interes
            mulValue = float(request.POST['value5'])
            
            result = 0
            if (capitalInitialValue == 0 and capitalFinalValue == 0 and taxValue == 0 and mulValue!=0 and taxRateValue!=0):
                result = (mulValue/(taxRateValue/100))
            elif (taxValue == 0):
                taxValue = (capitalFinalValue - capitalInitialValue)
            else:
                result = taxValue/((capitalInitialValue)*(taxRateValue/100))
            print(result)
            result = round(result, 5)
            result = str(result) + " Año(s)" + "\n - Meses: " + str(result*12) + "\n - Dias: " + str(result*365)
        except Exception as e:
            result = "Ocurrió un error: " + str(e)
        return render(request, 'result.html', {'result': result})
    return render(request, 'calculator.html')

# OK.
def calculate_compound_amount(request):
    if request.method == 'POST':
        try:
            result = {}
            # Capital
            capitalValue = float(request.POST['value1'])
            # % tasa de interes
            taxRateValue = float(request.POST['value2'])
            # tipo de interes
            taxTypeValue = request.POST.get('selectTaxRate')
            # tipo de capitalizacion
            capTypeValue = request.POST.get('selectCapValue')
            # Tiempo ---------------
            # dias
            days = int(request.POST['value3'])
            # meses
            months = int(request.POST['value4'])
            # años
            years = int(request.POST['value5'])
            # interes cambiante
            taxChangeRate = float(request.POST['value6'])
            # tipo de interes
            taxChangeTypeValue = request.POST.get('selectChangeTaxRate')
            # Tiempo cambiante ---------------
            # dias
            changedDays = int(request.POST['value7'])
            # meses
            changedMonths = int(request.POST['value8'])
            # años
            changedYears = int(request.POST['value9'])
            # llamar a la funcion para obtener el resultado
            calculate_result_compound(capitalValue, taxRateValue, taxTypeValue, capTypeValue, days, months, years, taxChangeRate, taxChangeTypeValue, changedDays, changedMonths, changedYears)
            result = calculate_result_compound(capitalValue, taxRateValue, taxTypeValue, capTypeValue, days, months, years, taxChangeRate, taxChangeTypeValue, changedDays, changedMonths, changedYears)
        except Exception as e:
            result['error'] = "Ocurrió un error: " + str(e)
        return render(request, 'result.html', {'result': result})
    return render(request, 'calculator2.html')

# OK.
def calculate_result_compound(capitalValue, taxRateValue, taxTypeValue, capTypeValue, days, months, years, taxChangeRate, taxChangeTypeValue, changedDays, changedMonths, changedYears):
    time = 0
    result = {'mainresult': 0, 'changedresult': None}
    taxRateValue = (taxRateValue/100)
    if (capTypeValue == None):
        # perform the basic formula
        if (taxTypeValue == "ti_anual"):
            time = convert_to_years(days, months, years)
        result['mainresult'] = (capitalValue*(1+time*taxRateValue))
    else:
        # perform the advanced formula
        if (capTypeValue == "cap_mensual"):
            time = convert_to_months(days, months, years)
            if (taxTypeValue == "ti_anual"):
                taxRateValue = taxRateValue/12
            result['mainresult'] = (capitalValue*((1+taxRateValue)**time))
            if (taxChangeRate != 0 ):
                taxChangeRate = (taxChangeRate/100)
                taxChangeRate = taxChangeRate/12
                timeChanged = convert_to_months(changedDays, changedMonths, changedYears)
                time = time-timeChanged
                result['mainresult'] = (capitalValue*((1+taxRateValue)**timeChanged))
                print(taxChangeRate)
                result['changedresult'] = (result['mainresult']*((1+taxChangeRate)**time))
                result['changedresult'] = str(round(result['changedresult'], 2)) + " $"
        elif (capTypeValue == "cap_anual"):
            time = convert_to_years(days, months, years)
    result['mainresult'] = str(round(result['mainresult'], 2)) + " $"
    return result

# OK.
def calculate_compound_capital(request):
    #capital 
    if request.method == 'POST':
        result = {}
        try:
            # Capital
            amountValue = float(request.POST['value1'])
            # % tasa de interes
            taxRateValue = float(request.POST['value2'])
            # tipo de interes
            taxTypeValue = request.POST.get('selectTaxRate')
            # tipo de capitalizacion
            capTypeValue = request.POST.get('selectCapValue')
            # Tiempo ---------------
            # dias
            days = int(request.POST['value3'])
            # meses
            months = int(request.POST['value4'])
            # años
            years = int(request.POST['value5'])
            result = calculate_result_ammound(amountValue, taxRateValue, taxTypeValue, capTypeValue, days, months, years)
        except Exception as e:
            result['error'] = "Ocurrió un error: " + str(e)
        return render(request, 'result.html', {'result': result})
    return render(request, 'calculator2.html')

# OK.
def calculate_result_ammound(amountValue, taxRateValue, taxTypeValue, capTypeValue, days, months, years):
    # cuanto capital depositó
    time = 0
    result = {}
    taxRateValue = (taxRateValue/100)
    if (capTypeValue == None):
        # perform the basic formula
        if (taxTypeValue == "ti_anual"):
            time = convert_to_years(days, months, years)
    else:
        # perform the advanced formula
        if (capTypeValue == "cap_mensual"):
            time = convert_to_months(days, months, years)
            if (taxTypeValue == "ti_anual"):
                taxRateValue = taxRateValue/12
        elif (capTypeValue == "cap_anual"):
            time = convert_to_years(days, months, years)
    result['mainresult'] = (amountValue/((1+taxRateValue)**time))
    result['mainresult'] = str(round(result['mainresult'], 2)) + " $"
    return result

# OK.
def calculate_compound_tax_rate(request):
    if request.method == 'POST':
        try:
            # Monto Compuesto
            amountValue = float(request.POST['value1'])
            # Capital
            capitalValue = float(request.POST['value2'])
            # tipo de capitalizacion
            capTypeValue = request.POST.get('selectCapValue')
            # Tiempo ---------------
            # dias
            days = int(request.POST['value3'])
            # meses
            months = int(request.POST['value4'])
            # años
            years = int(request.POST['value5'])
            
            result = calculate_result_tax_rate(amountValue, capitalValue, capTypeValue, days, months, years)
        except Exception as e:
            result['error'] = "Ocurrió un error: " + str(e)
        return render(request, 'result.html', {'result': result})
    return render(request, 'calculator2.html')

# OK.
def calculate_result_tax_rate(amountValue, capitalValue, capTypeValue, days, months, years):
    # cuanto capital depositó
    time = 0
    result = {}
    if (capTypeValue == None):
        # perform the basic formula
        print("TODO")
    else:
        # perform the advanced formula
        if (capTypeValue == "cap_mensual"):
            time = convert_to_months(days, months, years)
        elif (capTypeValue == "cap_anual"):
            time = convert_to_years(days, months, years)
    print((amountValue/capitalValue))
    print((1/time))
    print((amountValue/capitalValue)**(1/time))
    result['mainresult'] = (((amountValue/capitalValue)**(1/time))-1)*100
    
    result['mainresult'] = str(round(result['mainresult'], 3)) + " %"
    return result

# OK.
def calculate_compound_time(request):
    if request.method == 'POST':
        result = {}
        try:
            # Monto Compuesto
            amountValue = float(request.POST['value1'])
            # Capital
            capitalValue = float(request.POST['value2'])
            # % tasa de interes
            taxRateValue = float(request.POST['value3'])
            # tipo de interes
            taxTypeValue = request.POST.get('selectTaxRate')
            # tipo de capitalizacion
            capTypeValue = request.POST.get('selectCapValue')
            result = calculate_result_time(amountValue, capitalValue, taxRateValue, taxTypeValue, capTypeValue)
        except Exception as e:
            result['error'] = "Ocurrió un error: " + str(e)
        return render(request, 'result.html', {'result': result})
    return render(request, 'calculator2.html')

# OK.
def calculate_result_time(amountValue, capitalValue, taxRateValue, taxTypeValue, capTypeValue):
    result = {}
    taxRateValue = (taxRateValue/100)
    if (capTypeValue == None):
        # perform the basic formula
        result['mainresult'] = ((math.log(amountValue)/math.log(10))-(math.log(capitalValue)/math.log(10)))/(math.log(1+taxRateValue)/math.log(10))
    else:
        # perform the advanced formula
        if (capTypeValue == "cap_mensual"):
            print("Save")
            if (taxTypeValue == "ti_anual"):
                taxRateValue = taxRateValue/12
            result['mainresult'] = ((math.log(amountValue)/math.log(10))-(math.log(capitalValue)/math.log(10)))/(math.log(1+taxRateValue)/math.log(10))
        elif (capTypeValue == "cap_anual"):
            print("TODO")
    result['mainresult'] = str(round(result['mainresult'], 2)) + ""
    return result

# OK.
def convert_to_months(days, months, years):
    return days/30 + months + years*12

# OK.
def convert_to_days(days, months, years):
    return days+months*30+years*365

# OK.
def convert_to_years(days, months, years):
    return days/365 + months/12 + years

def amount_anuality(request):
    return render(request, "calculator3/amount_anuality.html")

def rent_anuality(request):
    return render(request, "calculator3/rent_anuality.html")

def tax_anuality(request):
    return render(request, "calculator3/tax_anuality.html")

def term_anuality(request):
    return render(request, "calculator3/term_anuality.html")

def calculate_amound_anuality(request):
    if request.method == 'POST':
        result = {}
        try:
            # renta
            rentValue = float(request.POST['value1'])
            # tipo de renta
            rentTypeValue = request.POST.get('selectRentRate')
            # tasa de interes
            taxRateValue = float(request.POST['value2'])
            # tipo de tasa de interes
            taxTypeValue = request.POST.get('selectTaxRate')
            # capitalizacion
            capTypeValue = request.POST.get('selectCapValue')
            # ----------------- Tiempo ---------------
            # dias
            days = int(request.POST['value3'])
            # meses
            months = int(request.POST['value4'])
            # años
            years = int(request.POST['value5'])
            
            result = result_amound_anuality(rentValue, taxRateValue, taxTypeValue, capTypeValue, days, months, years)
        except Exception as e:
            result['error'] = "Ocurrió un error: " + str(e)
        return render(request, 'result.html', {'result': result})
    return render(request, 'calculator3.html')

def result_amound_anuality(rentValue, taxRateValue, taxTypeValue, capTypeValue, days, months, years):
    time = 0
    result = {}
    taxRateValue = taxRateValue / 100
    
    if (taxTypeValue == "ti_anual"):
        if (capTypeValue == "cap_mensual"):
            time = convert_to_months(days, months, years)
        time = convert_to_years(days, months, years)
        
    elif (taxTypeValue == "ti_semestral"):
        time = convert_to_semesters(days, months, years)
    elif (taxTypeValue == "ti_mensual"):
        time = convert_to_months(days, months, years)

    # Calculando el capital requerido
    result['mainresult'] = rentValue * ((((1 + taxRateValue) ** time)-1) / taxRateValue)
    result['mainresult'] = str(round(result['mainresult'], 2)) + "$"
    return result

def calculate_rent_anuality(request):
    if request.method == 'POST':
        result = {}
        try:
            # Valor de monto o capital
            montValue = float(request.POST['value1'])
            # tipo de inversion
            investTypeValue = request.POST.get('selectInvestRate')
            # tasa de interes
            taxRateValue = float(request.POST['value2'])
            # tipo de tasa de interes
            taxTypeValue = request.POST.get('selectTaxRate')
            # ----------------- Tiempo ---------------
            # dias
            days = int(request.POST['value3'])
            # meses
            months = int(request.POST['value4'])
            # años
            years = int(request.POST['value5'])
            
            result = result_rent_anuality(montValue, investTypeValue, taxRateValue, taxTypeValue,  days, months, years)
        except Exception as e:
            result['error'] = "Ocurrió un error: " + str(e)
        return render(request, 'result.html', {'result': result})
    return render(request, 'calculator3.html')

def result_rent_anuality(montValue, investTypeValue, taxRateValue, taxTypeValue, days, months, years):
    time = 0
    result = {}
    taxRateValue = taxRateValue / 100
    
    if (taxTypeValue == "ti_anual"):
        if (investTypeValue == "cap_mensual"):
            time = convert_to_months(days, months, years)
        time = convert_to_years(days, months, years)
    elif (taxTypeValue == "ti_semestral"):
        time = convert_to_semesters(days, months, years)
        print(time)
    elif (taxTypeValue == "ti_mensual"):
        time = convert_to_months(days, months, years)

    # Calculando la renta
    result['mainresult'] = montValue / ((((1+taxRateValue)**time)-1)/taxRateValue)
    result['mainresult'] = str(round(result['mainresult'], 2)) + "$"
    return result

def calculate_capital_anuality(request):
    if request.method == 'POST':
        result = {}
        try:
            # renta
            rentValue = float(request.POST['value1'])
            # tasa de interes
            taxRateValue = float(request.POST['value2'])
            # tipo de tasa de interes
            taxTypeValue = request.POST.get('selectTaxRate')
            # capitalizacion
            capTypeValue = request.POST.get('selectCapValue')
            # ----------------- Tiempo ---------------
            # dias
            days = int(request.POST['value3'])
            # meses
            months = int(request.POST['value4'])
            # años
            years = int(request.POST['value5'])
            # enganche
            engancheValue = float(request.POST['value6'])
            
            result = result_capital_anuality(rentValue, taxRateValue, taxTypeValue, capTypeValue, days, months, years, engancheValue)
        except Exception as e:
            result['error'] = "Ocurrió un error: " + str(e)
        return render(request, 'result.html', {'result': result})
    return render(request, 'calculator3.html')
    
def result_capital_anuality(rentValue, taxRateValue, taxTypeValue, capTypeValue, days, months, years, enganche):
    time = 0
    result = {}
    taxRateValue = taxRateValue / 100
    
    if (taxTypeValue == "ti_anual"):
        time = convert_to_years(days, months, years)
        if (capTypeValue == "cap_mensual"):
            time = convert_to_months(days, months, years)
        
    elif (taxTypeValue == "ti_semestral"):
        time = convert_to_semesters(days, months, years)
    elif (taxTypeValue == "ti_mensual"):
        time = convert_to_months(days, months, years)

    # Calculando el capital requerido
    result['mainresult'] = rentValue * ((1-((1+taxRateValue/time)**(-time)))/(taxRateValue/time)) + enganche

    result['mainresult'] = str(round(result['mainresult'], 2)) + "$"
    return result

def convert_to_semesters(days, months, years):
    return days/182.5+months/6+years*2