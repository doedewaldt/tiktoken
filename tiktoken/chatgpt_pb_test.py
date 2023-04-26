import tkinter as tk
from tkinter import ttk
import psycopg

class DataWindow(tk.Frame):
    def __init__(self, master=None, connection_params=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.connection_params = connection_params
        self.create_widgets()

    def create_widgets(self):
        # Detail section
        self.detail_frame = tk.Frame(self.master, height=808, bg='#808080')
        self.detail_frame.pack(fill=tk.BOTH, expand=True)

        # Add Owning Agency text label
        self.owning_agency_label = tk.Label(self.detail_frame, text="Owning Agency", font=("Arial", 12))
        self.owning_agency_label.place(x=1426, y=600)

        # Add unitcostmethod column
        self.unitcostmethod_label = tk.Label(self.detail_frame, text="Unit Cost Method", font=("Arial", 12), bg="white", relief="groove")
        self.unitcostmethod_label.place(x=530, y=600, width=855, height=80)

        # Add Funding Source text label
        self.funding_source_label = tk.Label(self.detail_frame, text="Funding Source", font=("Arial", 12))
        self.funding_source_label.place(x=0, y=400)

        # Add Program Group text label
        self.program_label = tk.Label(self.detail_frame, text="Program Group", font=("Arial", 12))
        self.program_label.place(x=0, y=300)

        # Add Activity Group text label
        self.activity_group_label = tk.Label(self.detail_frame, text="Activity Group", font=("Arial", 12))
        self.activity_group_label.place(x=0, y=212)

        # Add Type of Activity text label
        self.type_of_activity_label = tk.Label(self.detail_frame, text="Type of Activity", font=("Arial", 12))
        self.type_of_activity_label.place(x=0, y=600)

        # Add Napis Group text label
        self.napis_group_label = tk.Label(self.detail_frame, text="Napis Group", font=("Arial", 12))
        self.napis_group_label.place(x=0, y=500)

        # Add Activity Number text label
        self.activity_number_label = tk.Label(self.detail_frame, text="Activity Number", font=("Arial", 10), fg="#FFFFFF")
        self.activity_number_label.place(x=0, y=4)

        # Add Activity column
        self.activity_column = ttk.Entry(self.detail_frame, width=30)
        self.activity_column.place(x=530, y=4)

        # Add Activity Name text label
        self.activity_name_label = tk.Label(self.detail_frame, text="Activity Name", font=("Arial", 12))
        self.activity_name_label.place(x=0, y=100)

        # Add provider_id column as a ComboBox
        self.provider_id_var = tk.StringVar()
        self.provider_id_combo = ttk.Combobox(self.detail_frame, textvariable=self.provider_id_var, width=30)
        self.provider_id_combo.place(x=1957, y=600)
        self.provider_id_combo['values'] = ('Provider 1', 'Provider 2', 'Provider 3')  # Example values

        # Add service column as a ComboBox
        self.service_var = tk.StringVar()
        self.service_combo = ttk.Combobox(self.detail_frame, textvariable=self.service_var, width=30)
        self.service_combo.place(x=530, y=200)
        self.service_combo['values'] = ('Service 1', 'Service 2', 'Service 3')  # Example values

        # Add program column as a ComboBox
        self.program_var = tk.StringVar()
        self.program_combo = ttk.Combobox(self.detail_frame, textvariable=self.program_var, width=30)
        self.program_combo.place(x=530, y=300)
        self.program_combo['values'] = ('Program 1', 'Program 2', 'Program 3')  # Example values

        # Add funding_source column as a ComboBox
        self.funding_source_var = tk.StringVar()
        self.funding_source_combo = ttk.Combobox(self.detail_frame, textvariable=self.funding_source_var, width=30)
        self.funding_source_combo.place(x=530, y=400)
        self.funding_source_combo['values'] = ('Funding Source 1', 'Funding Source 2', 'Funding Source 3')  # Example values

        # Add category column as a ComboBox
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(self.detail_frame, textvariable=self.category_var, width=30)
        self.category_combo.place(x=530, y=500)
        self.category_combo['values'] = ('Category 1', 'Category 2', 'Category 3')  # Example values

        # Add description column as an Entry
        self.description_var = tk.StringVar()
        self.description_entry = tk.Entry(self.detail_frame, textvariable=self.description_var, width=30)
        self.description_entry.place(x=530, y=100)

        # Add "Activity Last Modified" label
        self.activity_last_modified_label = tk.Label(self.detail_frame, text="Activity Last Modified:")
        self.activity_last_modified_label.place(x=55, y=708)

        # Add "Activity Created" label
        self.activity_created_label = tk.Label(self.detail_frame, text="Activity Created:")
        self.activity_created_label.place(x=1317, y=708)

        # Add created column as a Label
        self.created_var = tk.StringVar()
        self.created_label = tk.Label(self.detail_frame, textvariable=self.created_var)
        self.created_label.place(x=1792, y=708)

        # Add lupdate column as a Label
        self.lupdate_var = tk.StringVar()
        self.lupdate_label = tk.Label(self.detail_frame, textvariable=self.lupdate_var)
        self.lupdate_label.place(x=677, y=708)

        # Add nsip column as a Checkbutton
        self.nsip_var = tk.BooleanVar()
        self.nsip_checkbutton = tk.Checkbutton(self.detail_frame, text="NSIP", variable=self.nsip_var)
        self.nsip_checkbutton.place(x=987, y=4)

        # Add "Transfer" label
        self.transfer_label = tk.Label(self.detail_frame, text="Transfer", bg="grey")
        self.transfer_label.place(x=1298, y=4)

        # Add transfer column as an OptionMenu
        self.transfer_var = tk.StringVar()
        transfer_options = ['Option 1', 'Option 2', 'Option 3']  # Add your options here
        self.transfer_var.set(transfer_options[0])  # Set the default selection
        self.transfer_optionmenu = tk.OptionMenu(self.detail_frame, self.transfer_var, *transfer_options)
        self.transfer_optionmenu.config(bg="white", bd=5)
        self.transfer_optionmenu.place(x=1582, y=4, width=229, height=22)

        # Add status column as a Checkbutton with dynamic background color
        self.status_var = tk.BooleanVar()
        self.status_checkbutton = tk.Checkbutton(self.detail_frame, text="make activity inactive", variable=self.status_var)
        self.status_checkbutton.place(x=2834, y=4, height=22)

        def update_status_bg_color():
            if self.status_var.get():
                bg_color = "tomato"
            else:
                bg_color = "pale green"
            self.status_checkbutton.config(bg=bg_color)
            self.detail_frame.after(100, update_status_bg_color)

        update_status_bg_color()

        # Add "System Recommends you" label with dynamic visibility
        def update_recommend_label_visibility():
            visible = False  # Change this condition to your desired visibility condition
            if visible:
                self.recommend_label.place(x=2048, y=4)
            else:
                self.recommend_label.place_forget()
            self.detail_frame.after(100, update_recommend_label_visibility)

        self.recommend_label = tk.Label(self.detail_frame, text="System Recommends you", bg="yellow")
        update_recommend_label_visibility()

        # Add "Units Last Updated:" label
        self.units_last_updated_label = tk.Label(self.detail_frame, text="Units Last Updated:", bg="light grey")
        self.units_last_updated_label.place(x=2432, y=708)

        # Add compute element (last_used)
        last_used = "2019-08-15 14:35"  # Replace this with the actual last_used value
        last_used_label = tk.Label(self.detail_frame, text=last_used, bg="light grey")
        last_used_label.place(x=2962, y=708)

        # Create the export buttons frame
        export_buttons_frame = tk.Frame(self.master)
        export_buttons_frame.pack(side="bottom", pady=10)

        # Functions for export buttons (you need to implement the export functionality)
        def export_to_xml():
            print("Exporting to XML...")

        def export_to_pdf():
            print("Exporting to PDF...")

        def export_to_xhtml():
            print("Exporting to XHTML...")

        # Add Export to XML button
        export_xml_button = tk.Button(export_buttons_frame, text="Export to XML", command=export_to_xml)
        export_xml_button.pack(side="left", padx=5)

        # Add Export to PDF button
        export_pdf_button = tk.Button(export_buttons_frame, text="Export to PDF", command=export_to_pdf)
        export_pdf_button.pack(side="left", padx=5)

        # Add Export to XHTML button
        export_xhtml_button = tk.Button(export_buttons_frame, text="Export to XHTML", command=export_to_xhtml)
        export_xhtml_button.pack(side="left", padx=5)

        # Create Treeview for table columns
        self.columns = [
            "category", "funding_source", "program", "service", "activity", "description",
            "unitcostmethod", "provider_id", "transfer", "nsip", "status", "lupdate",
            "created", "last_service_used", "last_service_group_used", "last_used"
        ]

        self.tree = ttk.Treeview(self.detail_frame, columns=self.columns, show="headings")

        for col in self.columns:
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Retrieve data from database
        self.fetch_data()

    def fetch_data(self):
        # Replace these placeholders with your PostgreSQL connection information
        if not self.connection_params:
            self.connection_params = {
                "host": "your_host",
                "port": "your_port",
                "dbname": "your_database_name",
                "user": "your_username",
                "password": "your_password"
            }

        # conn = psycopg.connect(**self.connection_params)

        aActivity = 1  # Replace this with the actual activity number value
        query = '''
            SELECT
                activity.funding_source,
                activity.program,
                activity.service,
                activity.activity,
                activity.description,
                activity.unitcostmethod,
                activity.provider_id,
                activity.transfer,
                activity.nsip,
                activity.status,
                activity.lupdate,
                activity.created,
                (SELECT MAX(lupdate) FROM service WHERE service.activity = activity.activity) AS last_service_used,
                (SELECT MAX(lupdate) FROM service_group WHERE service_group.activity = activity.activity) AS last_service_group_used,
                CASE
                    WHEN last_service_used IS NOT NULL AND last_service_group_used IS NOT NULL THEN
                        GREATEST(last_service_used, last_service_group_used)
                    ELSE
                        COALESCE(last_service_used, last_service_group_used)
                END AS last_used
            FROM activity_all AS activity
            WHERE activity.activity = %s
        '''

        # with conn.cursor() as cur:
        #     cur.execute(query, (aActivity,))
        #     rows = cur.fetchall()

        # for row in rows:
        #     self.tree.insert('', 'end', values=row)

        # conn.close()

root = tk.Tk()
app = DataWindow(master=root)
app.mainloop()
