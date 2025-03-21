#Author: Thewan Chanmina Jayaweera
#Date: 23/12/2024

# Task D: Histogram Display
import tkinter as tk
import csv
import os

class HistogramApp:
    def __init__(self, traffic_data, date):
        """
        Initializes the histogram application with the traffic data and selected date.
        """
        self.root = tk.Tk()
        self.traffic_data = traffic_data
        self.date = date
        self.elmvehicle_volume = [0] * 24  #Initialize hourly counts for Elm Avenue
        self.hanleyvehicle_volume = [0] * 24 #Initialize hourly counts for Hanley Highway
        self.root.title("Histogram") # Title of the window

    def setup_window(self):
        """
        Sets up the Tkinter window and canvas for the histogram.
        """
       
        # Create a canvas
        self.canvas_width = 1200  #Canvas width
        self.canvas_height = 600  #Canvas Height
        self.canvas = tk.Canvas(width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()
        return self.canvas

        
    def load_data(self):
        try:
            with open("C:\\Users\\STZ\\Desktop\\VIVA\\w2121370 (1)\\"+ self.traffic_data, 'r') as file:
                reader = csv.DictReader(file)  # Use DictReader to read data as rows
               
                # Process the rows to update hourly vehicle counts
                for row in reader:
                    try:
                        hour = int(row["timeOfDay"].split(":")[0])  # Extract the hour from timeOfDay
                        if row["JunctionName"] == "Elm Avenue/Rabbit Road":
                            self.elmvehicle_volume[hour] += 1 #Updates the count in corresponding hour in the array 
                        elif row["JunctionName"] == "Hanley Highway/Westway":
                            self.hanleyvehicle_volume[hour] += 1 #Updates the count in corresponding hour in the array
                    except (KeyError, ValueError) as e:
                        print(f"Error processing row: {row} - {e}") 
        except Exception as e:
            print(f"Error loading data: {e}") 


    def draw_histogram(self):
        """
        Draws the histogram with axes, labels, and bars.
        """
        max_value = max(max(self.elmvehicle_volume), max(self.hanleyvehicle_volume)) #Max value out of the two arrays is selected as the tallest bar 
        bar_width = self.canvas_width / 54  # Divide evenly for to fit all the bars inside the canvas
       
        # Title
        self.canvas.create_text(300, 30, text=f"Histogram of Vehicle Frequency per Hour ({self.date})", font=("Arial", 16))
        #Gives a title to the histogram 
       
        # Draw bars
        for hour in range(24):  # 0 to 23 hours

            spacing = 3
            # Elm Avenue bar
            x0_elm = hour * (2 * bar_width + spacing) + 50  #x-coordinates of the Elm-Avenue bar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
            y0_elm = self.canvas_height - (self.elmvehicle_volume[hour] / max_value) * 400 if max_value else self.canvas_height - 50
            x1_elm = x0_elm + bar_width
            self.canvas.create_rectangle(x0_elm, y0_elm, x1_elm, self.canvas_height - 30, fill="lightgreen")
            self.canvas.create_text((x0_elm+10) ,y0_elm - 7,text=str(self.elmvehicle_volume[hour]), font=("Arial", 10)) #Gives the hourly count as a label at the top of the bar 
           
            # Hanley Highway bar
            x0_hanley = x1_elm  #Hanley Highway bar is right next to Elm Avenue bar; so it has the end coordinates of Elm bar as it's starting coordinate
            y0_hanley = self.canvas_height - (self.hanleyvehicle_volume[hour] / max_value) * 400 if max_value else self.canvas_height - 50
            x1_hanley = x0_hanley + bar_width
            self.canvas.create_rectangle(x0_hanley, y0_hanley, x1_hanley, self.canvas_height - 30, fill="lightcoral")
            self.canvas.create_text(x0_hanley+10 ,y0_hanley - 7,text=str(self.hanleyvehicle_volume[hour]), font=("Arial", 10)) #Gives the hourly count as a label at the top of the bar
           
            # Add hour label
            self.canvas.create_text((x0_elm + x1_hanley) / 2, self.canvas_height - 20, text=str(hour), font=("Arial", 10)) #Adds the corresponding hour label below the x-axis for reference
            


    def add_legend(self):
        """
        Adds a legend to the histogram to indicate which bar corresponds to which junction.
        """
        # Axes and Legend
        self.canvas.create_line(50, self.canvas_height - 30, self.canvas_width-200, self.canvas_height - 30)  # creates a line to represent x-axis
        self.canvas.create_text(550, self.canvas_height-5, text="Hours (00:00 - 24:00)",font=("Arial", 12), anchor="w") #Creates a text that says "Hours (00:00 - 24:00)" below the x axis and labels
       
        # Legend
        self.canvas.create_rectangle(50, 60, 70, 80, fill="lightgreen")
        self.canvas.create_text(90, 70, text="Elm Avenue/Rabbit Road", anchor="w")
       
        self.canvas.create_rectangle(50, 90, 70, 110, fill="lightcoral")
        self.canvas.create_text(90, 100, text="Hanley Highway/Westway", anchor="w")

        #Creates small rectangles with the respective colours and a text to represent each junction at the top right 

    def run(self):
        """
        Runs the Tkinter main loop to display the histogram.
        """
        self.setup_window()
        self.load_data()
        self.draw_histogram()
        self.add_legend()
        self.root.mainloop()

        #Initializes and displays the histogram GUI 

# Task E: Code Loops to Handle Multiple CSV Files
class MultiCSVProcessor:
    def __init__(self):
        """
        Initializes the application for processing multiple CSV files.
        """
        self.current_data = None

    def validate_date_input(self):
        while True:
            try:
                while True:
                    try:
                        day = int(input("Please enter the day of the survey in the format DD: "))
                        if day < 1 or day > 31:
                            print("Out of range")
                        else:
                            break
                        
                    except ValueError:
                        print("Integer required")

                while True:
                    try:
                        month = int(input("Please enter the month of the survey in the format MM: "))
                        if month < 1 or month > 12:
                            print("Out of range")
                        else:
                            break
                        
                    except ValueError:
                        print("Integer required")
                        
                while True:
                    try:
                        year = int(input("Please enter the year of the survey in the format YYYY: "))
                        if year < 2000 or year > 2024:
                            print("Out of range")
                        else:
                            break
                        
                    except ValueError:
                        print("Integer required")

                date = f"{day:02}/{month:02}/{year}"
                print("Validated date: ",date)
                return date
            
            except ValueError:
                print("Integer required")

                #While-True loops makes sure the three inputs are within the accepted range of values and if not, re-prompts the user to enter the a valid value.
                #Try-Except blocks are used for each input to avoid repeating the whole prompt process when a non-integer input is entered.


    def load_csv_file(self,date):
        """
        Loads a CSV file and processes its data.
        """


        file1 = "traffic_data15062024.csv"
        file2 = "traffic_data16062024.csv"
        file3 = "traffic_data21062024.csv"

        #The three csv files are assigned to variables named file1,file2 and file3 respectively
        validate_date = date
        try:
            if validate_date == "15/06/2024":
                traffic_datafile = file1
            elif validate_date == "16/06/2024":
                traffic_datafile = file2
            elif validate_date == "21/06/2024":
                traffic_datafile = file3
            else:
                traffic_data = ""
            return traffic_datafile

        #The csv file is assigned to it's corresponding date (eg: If the validated date is 15/06/2024 , "traffic_data15062024.csv" is assigned to it)
        #"With open()" command opens the file after the validated date is processed in the above steps
        #Since all three files are located in the same folder, they have the same path.
        #"traffic_datafile" which is introduced in the above step is then combined with the path("D:\\SD1 Coursework 01\\") to create the complete path.
                
        except FileNotFoundError:
            print("Error: Traffic data for the selected date is not available")

        #Try-Except block handles exceptions(when a database is not available for the requested date, "Error: Traffic data for the selected date is not available" will be displayed on the shell window)
            

    def clear_previous_data(self):
        """
        Clears data from the previous run to process a new dataset.
        """

        os.system('cls')

        #This command clears the data of previous run from the terminal if the user wishes to load a new dataset. Note that this works only on the terminal 


    def handle_user_interaction(self):
        """
        Handles user input for processing multiple files.
        """

        while True:
            option = input("\nDo you want to load another dataset? (Y/N): ").upper()
            if option == 'Y':
                self.clear_previous_data()
                break
                
            elif option == 'N':
                print("Exiting....")
                return option
            
            elif option not in ["Y","N"]:
                print("Invalid input. Please enter 'Y' for YES and 'N' for NO")

 
    def process_files(self,traffic_datafile):
        """
        Main loop for handling multiple CSV files until the user decides to quit.
        """

        total_vehicles = 0
        total_trucks = 0
        total_electricvehicles = 0
        twowheeled_vehicles = 0
        total_buses = 0
        without_turning = 0
        total_bicycles = 0
        over_speed = 0
        elm_vehicles = 0
        elm_scooters = 0
        hanley_vehicles = 0
        peakhour_vehicles = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        busiest_hours = []
        busiest_hour_from_to = ""
        #The variables required for the calculations are introduced above with their values set to "0" as most of them are counters which are to be incremented with each iteration
        
        with open("C:\\Users\\STZ\\Desktop\\VIVA\\w2121370 (1)\\" +traffic_datafile) as file:
            reader = csv.DictReader(file)
            #This command is used to read each row in the csv file as a dictionary where the keys are the header of the row and the values are the entries that follow them
            #"file.seek(0)" command used below is used to bring the cursor back to beginning of the file to re-read the file after reading through it once.


            for row in reader:
                total_vehicles += 1
                #Counts the total number of vehicles passing through all junctions
                    
                    
            file.seek(0)
            for row in reader:
                if row["VehicleType"]== "Truck":
                    total_trucks += 1
                    #Counts the total number of trucks passing through all junctions

            file.seek(0)       
            for row in reader:
                if row["elctricHybrid"]== "True":
                    total_electricvehicles += 1
                    #Counts the total number of electric vehicles passing through all junctions
                
            file.seek(0)
            for row in reader:
                if row["VehicleType"] in ["Bicycle","Motorcycle","Scooter"]:
                    #Two-wheeled vehicles(Bicycles ,motorcycles and scooters are introduced as 
                    twowheeled_vehicles += 1
                    #Counts the number of “two wheeled” vehicles(bicycles,motorcycles or scooters) through all junctions

            file.seek(0)
            for row in reader:
                if row["VehicleType"] == "Buss" and row["JunctionName"]== "Elm Avenue/Rabbit Road" and row["travel_Direction_out"]== "N" :
                    total_buses += 1
                    #Counts the total number of busses leaving Elm Avenue/Rabbit Road junction heading north
                        
            file.seek(0)
            for row in reader:
                if row["travel_Direction_in"]== row["travel_Direction_out"]:
                    without_turning += 1
                    #Counts the total number of vehicles passing through both junctions without turning left or right


            try:
                truck_percentage = round((total_trucks/total_vehicles)*100)
            except ZeroDivisionError:
                print("No trucks have been recorded")
            #Calculates the percentage of all vehicles recorded that are Trucks for the selected date (rounded to an integer)

            file.seek(0)
            for row in reader:
                if row["VehicleType"] == "Bicycle":
                    total_bicycles += 1
                    bicycles_perhour = int(total_bicycles/24)
                           
            #Calculates the average number Bicycles per hour for the selected date (rounded to an integer)

            file.seek(0)
            for row in reader:
                if row["VehicleSpeed"].isdigit() and row["JunctionSpeedLimit"].isdigit():
                    if int(row["VehicleSpeed"]) > int(row["JunctionSpeedLimit"]):
                        over_speed += 1
                else:
                    continue
                #Counts the total number of vehicles recorded as over the speed limit for the selected date

            file.seek(0)
            for row in reader:
                if row["JunctionName"]== "Elm Avenue/Rabbit Road":
                    elm_vehicles += 1
                    #Counts the total number of vehicles recorded through only Elm Avenue/Rabbit Road junction
                
            file.seek(0)
            for row in reader:
                if row["JunctionName"]== "Hanley Highway/Westway":
                    hanley_vehicles += 1
                    #Counts the total number of vehicles recorded through only Hanley Highway/Westway junction

            file.seek(0)
            for row in reader:
                if row["JunctionName"]== "Elm Avenue/Rabbit Road" and row["VehicleType"]== "Scooter":
                    elm_scooters += 1
                    elmscooters_percentage = int((elm_scooters/elm_vehicles)*100)
                    #Calculates the percentage of vehicles through Elm Avenue/Rabbit Road that are Scooters (rounded to integer)
                     
            file.seek(0)
            for row in reader:
                if row["JunctionName"] == "Hanley Highway/Westway":
                    timeOfDay = row["timeOfDay"]
                    hour = int(timeOfDay.split(":")[0])
                    peakhour_vehicles[hour] += 1

                    #The relevant entries are sorted out from the condtion 'if row["JunctionName"] == "Hanley Highway/Westway"'
                    #The selected entries from the row "timeOfDay" is then assigned to a variable named "timeOfDay"
                    #These entries are then splitted at the colon ":" (eg: If timeOfDay = "6:46:17 AM" , the split command generates a list ["6" , "46" , "17 AM"]
                    #In "timeOfDay.split(":")[0]" indexing is used to extract the hour from the entry.(eg: zeroth element of the list["6" , "46" , "17 AM"] is "6" )
                    #"int()" converts the hour string into an integer
                    #"peakhour_vehicles[hour] += 1" increments the count of vehicles for each hour
                        

            max_vehicles = max(peakhour_vehicles)
            #Counts the number of vehicles recorded in the peak (busiest) hour on Hanley Highway/Westway by finding the maximum value from the dictionary "peakhour_vehicles"
                
            hour = 0

            for count in peakhour_vehicles:
                if count == max_vehicles:
                    busiest_hours.append(hour)
                hour += 1

            for hour in busiest_hours:
                busiest_hour_from_to += f"{hour}:00 and {hour+1}:00"
                     
            #Evaluates the time or times of the peak (busiest) traffic hour (or hours) on Hanley Highway/Westway in the format Between 18:00 and 19:00.
                    
            try:
                totalhours_rain = set()
                file.seek(0)
                for row in reader:
                    if row["Weather_Conditions"] in ["Light Rain" , "Heavy Rain"]:
                        timeOfDay = row["timeOfDay"]
                        hours = int(timeOfDay.split(":")[0])
                        totalhours_rain.add(hours)
                            
                #totalhours_rain is an empty set which was introduced earlier along with the variables
                #Hour is extracted from the entries after splitting
                #"totalhours_rain.add(hours)" adds the hour to the empty set 'totalhours_rain'
                #Using a set allows us to avoid duplicating the same value twice (eg: If there are entries for 8:30 AM and 8.45 AM, it will only update 8 once in the set)
                            
                total_hours_of_rain = len(totalhours_rain)
                #This gives the number of elements that are stored in the set
            except Exception as e:
                print()
                   
                #Counts the total number of hours of rain on the selected date
                    

            outcomes = [traffic_datafile,total_vehicles,total_trucks,total_electricvehicles,twowheeled_vehicles,total_buses,without_turning,truck_percentage,bicycles_perhour,over_speed,elm_vehicles,hanley_vehicles,elmscooters_percentage,max_vehicles,busiest_hour_from_to,total_hours_of_rain]
            return outcomes

        #The outcomes from Task B are stored in a list because it is easy to use access those outcomes by indexing method


    def display_outcomes(self,outcomes):
        #The list named "outcomes" which was introduced eariler is used inside this function to print the outcomes to the shell window. Indexing is used in this case
        print("\n")
        print("*"*46)
        print(f"Data file selected is {outcomes[0]}")
        print("*"*46)
        print(f"\nThe total number of vehicles passing through all junctions:{outcomes[1]}")
        print(f"The total number of trucks passing through all junctions:{outcomes[2]}")
        print(f"The total number of electric vehicles passing through all junctions:{outcomes[3]}")
        print(f"The number of “two wheeled” vehicles through all junctions:{outcomes[4]}")
        print(f"The total number of busses leaving Elm Avenue/Rabbit Road junction heading north:{outcomes[5]}")
        print(f"The total number of vehicles passing through both junctions without turning left or right:{outcomes[6]}")
        print(f"The percentage of all vehicles recorded that are Trucks for the selected date (rounded to an integer):{outcomes[7]}%")
        print(f"The average number Bicycles per hour for the selected date (rounded to an integer):{outcomes[8]}")
        print(f"The total number of vehicles recorded as over the speed limit for the selected date:{outcomes[9]}")
        print(f"The total number of vehicles recorded through only Elm Avenue/Rabbit Road junction:{outcomes[10]}")
        print(f"The total number of vehicles recorded through only Hanley Highway/Westway junction:{outcomes[11]}")
        print(f"The percentage of vehicles through Elm Avenue/Rabbit Road that are Scooters (rounded to integer):{outcomes[12]}%")
        print(f"The number of vehicles recorded in the peak (busiest) hour on Hanley Highway/Westway:{outcomes[13]}")
        print(f"The peak (busiest) traffic hour (or hours) on Hanley Highway/Westway were recorded between: {outcomes[14]}")
        print(f"The total number of hours of rain on the selected date:{outcomes[15]}")
        print(f"\nResults have been succesfully saved to text file")
        #Prints all the above outcomes in the shell window

    def save_results_to_file(self,outcomes):
        try:
            with open("C:\\Users\\STZ\\Desktop\\VIVA\\w2121370 (1)\\results.txt",mode="a") as file:
                file.write("\n")
                file.write("*"*7)
                file.write("\n")
                file.write("Results")
                file.write("\n")
                file.write("*"*7)
                file.write("\n")
                file.write(f"\nData file selected is {outcomes[0]}")
                file.write(f"\nThe total number of vehicles passing through all junctions:{outcomes[1]}")
                file.write(f"\nThe total number of trucks passing through all junctions:{outcomes[2]}")
                file.write(f"\nThe total number of electric vehicles passing through all junctions:{outcomes[3]}")
                file.write(f"\nThe number of two wheeled vehicles through all junctions:{outcomes[4]}")
                file.write(f"\nThe total number of busses leaving Elm Avenue/Rabbit Road junction heading north:{outcomes[5]}")
                file.write(f"\nThe total number of vehicles passing through both junctions without turning left or right:{outcomes[6]}")
                file.write(f"\nThe percentage of all vehicles recorded that are Trucks for the selected date (rounded to an integer):{outcomes[7]}%")
                file.write(f"\nThe average number Bicycles per hour for the selected date (rounded to an integer):{outcomes[8]}")
                file.write(f"\nThe total number of vehicles recorded as over the speed limit for the selected date:{outcomes[9]}")
                file.write(f"\nThe total number of vehicles recorded through only Elm Avenue/Rabbit Road junction:{outcomes[10]}")
                file.write(f"\nThe total number of vehicles recorded through only Hanley Highway/Westway junction:{outcomes[11]}")
                file.write(f"\nThe percentage of vehicles through Elm Avenue/Rabbit Road that are Scooters (rounded to integer):{outcomes[12]}%")
                file.write(f"\nThe number of vehicles recorded in the peak (busiest) hour on Hanley Highway/Westway:{outcomes[13]}")
                file.write(f"\nThe peak (busiest) traffic hour (or hours) on Hanley Highway/Westway were recorded between: {outcomes[14]}")
                file.write(f"\nThe total number of hours of rain on the selected date:{outcomes[15]}")
                file.write("\n")
                file.write("."*167)
            file.close()
        except Exception as e:
            print()
            #Creates a text file named "Results.txt" and saves all the outcomes to the text file.


def main():
    instance = MultiCSVProcessor()
    while True:
        try:
            date = instance.validate_date_input()

            traffic_datafile = instance.load_csv_file(date)

            outcomes = instance.process_files(traffic_datafile)

            instance.display_outcomes(outcomes)

            instance.save_results_to_file(outcomes)

            app = HistogramApp(traffic_datafile,date)
            
            app.run()

            
            if instance.handle_user_interaction() == "N":
                break
        except (TypeError, UnboundLocalError) as e:
            print("An unknown error occured. Please try again")
            if (instance.handle_user_interaction()) == "N":
                break

main()

#An object of the class MultiCSVProcessor is created
#validate_date_input: Ensures the user provides a valid date.
#load_csv_file: Loads a CSV file based on the validated date.
#process_files: Processes the loaded CSV data.
#display_outcomes: Displays the processed results after processing the csv data
#save_results_to_file: Saves the results to a text file 
#HistogramApp Initialization: Creates an instance of HistogramApp with the data and date parameters.
#run: Displays the histogram using Tkinter
#Loops to ask if the user wants to load another dataset and if they don't, the loop breaks and the program ends
#Main function is called to execute the program



#REFERENCES

#ChatGPT - https://chatgpt.com/share/676632c2-1cd0-8011-860f-65afc94d06a3 , https://chatgpt.com/share/6742ed2b-d118-8011-b63f-0acbbfd4bc3d
#[Python GUI - 01 | Hello World Program | Sinhala] Available at: https://youtu.be/Myzo1pBsXeE?si=yzOSjGumYywm2iOw
#[Python GUI - 11 | Canvas | Sinhala] Available at: https://youtu.be/Myzo1pBsXeE?si=yzOSjGumYywm2iOw


    
