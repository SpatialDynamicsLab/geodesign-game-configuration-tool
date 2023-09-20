# Don't forget to install all the dependencies needed
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def create_db():
    conn = sqlite3.connect('config_generator.db')
    c = conn.cursor()

    # Create the 'cities' table
    c.execute('''CREATE TABLE IF NOT EXISTS cities (
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 description TEXT NOT NULL,
                 ebas TEXT NOT NULL,
                 mean_cost INTEGER NOT NULL,
                 currency TEXT NOT NULL,
                 location TEXT NOT NULL,
                 budget INTEGER NOT NULL
                 )''')

    # Create the 'ebas' table without explicit ID
    c.execute('''CREATE TABLE IF NOT EXISTS ebas (
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 description TEXT NOT NULL,
                 icon TEXT NOT NULL,
                 cost INTEGER NOT NULL
                 )''')

    conn.commit()
    conn.close()


def insert_initial_ebas():
    conn = sqlite3.connect('config_generator.db')
    c = conn.cursor()

    # Insert sample EBA data without UUID
    ebas_data = [
        ('Dune Stabilization', 'Dune stabilization refers to the process of managing and preserving sand dunes to prevent erosion and maintain their ecological and environmental functions...', 'Dune', 70000),
        ('Tree plantation', 'Tree plantation is the process of planting and establishing trees in various locations, including forests, urban areas, and agricultural lands, with the aim of improving the environment and achieving multiple benefits...', 'Green', 70000),
        ('Grasslands', 'Protection and restoration of areas dominated by a continuous cover of grasses, without the presence of taller plants such as trees or shrubs...', 'Grass', 70000),
        ('Filtering water', 'Grass drainage, designed to absorb water and reduce permanently drained and often impermeable areas...', 'Filter', 70000),
        ('Flood plain enlargement/restoration', 'Enlargement and restoration of river flood plains, consisting out of lowering the level and/or increasing the width of the flood plain area next to a riverbed...', 'Flood', 70000),
        ("Filtering water from the city's rooftops and parkings", "Multi-levelled gardens or parks with shallow depressions that use a special mix of sand and compost that allow water to soak in rapidly...", 'Filter', 70000),
        ('Cope with storms and floods', 'Landscape designed to catch water from a higher elevation and permanently hold run-off from melted water and precipitation...', 'Storm', 70000),
        ('Introduction and/or restoration of Bioswale', 'Landscape depression that receives and filters water runoffs back to the sewer water system through water-holding vegetation and organic materials...', 'Bioswale', 70000),
        ('Marram grass planting', 'Planting vegetation on sand dunes for coastal protection...', 'Grass', 70000),
        ('Peatland restoration', 'Restoration of the original peatland by rewetting the surface area through blocking canals, restoration of peat vegetation and planting of (resilient) peat species...', 'Peat', 70000),
        ('Seagrass meadow restoration', 'Seagrass meadows are underwater ecosystems formed by saltwater plants with roots and rhizomes anchored in the seafloor sand...', 'Seagrass', 70000),
        ('Estuaries protection and restoration', 'Protection and restoration of estuaries by providing stabilisation, reduce the force of incoming waves, while constituting an important source of carbon sequestration in coastal areas...', 'Estuary', 70000),
        ('River bed deepening', 'The lowering and deepening of the riverbed in order to accommodate greater depths of water to prevent overflow and thus flooding...', 'River', 70000),
        ('Dune restoration', 'Planting indigenous climate-resilient dune plants that pioneer revegetation, and will facilitate to naturally regenerate the dune ridge...', 'Dune', 70000),
        ('Linking ecosystems', 'Roads and paths (for motorized and non-motorized traffic respectively) aligned/bordered/surrounded with significant presence of vegetation, trees, and plants...', 'Link', 70000),
        ('Cultivate in town', 'Urban agriculture practices to grow crops or animals for personal consumption or to sell locally within and around cities...', 'Urban', 70000),
        ('Saltmarsh and mudflat management and restoration', 'Management and restoration of areas through hydrologic restoration/re-establishment of tidal hydrodynamics in saltmarshers and mudflats...', 'Saltmarsh', 70000),
        ('Promote water infiltration', 'Land depressions designed to have water-storage capacity and manage surface runoff water during rainfall events...', 'Infiltration', 70000)
    ]

    c.executemany('''INSERT INTO ebas (name, description, icon, cost)
                     VALUES (?, ?, ?, ?)''', ebas_data)

    conn.commit()
    conn.close()



@app.route("/")
def hello_world():
    return "<p>Database Created</p>"

if __name__ == '__main__':
    create_db()  # Create the database and tables when the app starts
    insert_initial_ebas()  # Insert initial EBA data without UUIDs
    app.run(debug=True)
