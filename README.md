# Patent Portfolio Dashboard

The dashboard is made to display the portfolio of System on Chip (SoC) patents from 3 main competitors (Intel, Samsung, TSMC). The data used are obtained from real sources but are filtered and scaled-down for demonstrative purpose.

### Viewing Deployed Site

> [!NOTE]
> Deployment is live, feel free to check it out. Or please deploy the repository locally to view.

[Click here](https://dash-patent-portfolio-a69935845d06.herokuapp.com/) to view the deployed dashboard.

## Technologies Used

The project mainly uses Python to program the interactive dashboard, using SQLite to create a database and queries, while Heroku was used to deploy the project.

[![Tech Stack](https://skillicons.dev/icons?i=heroku,py,sqlite)]()

In addition, [DB Browser](https://sqlitebrowser.org/) was used to test the SQL queries before they were used in the "app".

## Running the Code

> Note: You may deploy the project to your local as normal.

To run the code, you may open `app.py` and locate the following line:

```
if __name__ == '__main__':
    app.run(debug=True)
```

and change it to the following:

```
if __name__ == '__main__':
    app.run_server(debug=True)
```

You may then run the python file as normal, a local window of the dashboard should pop-up shortly afterward.

## Project Overview

Our dashboard are separated into 3 main sections:
- An overview of the 3 competitors in the SoC patenting market
- The patent trends
- Company's impact to the world (domestically and internationally)

In each section, some data visualizations are provided along with some interactable components in the section to view/filter data.

<p align = "center">
  <img src="https://github.com/user-attachments/assets/956de3dc-2695-4cea-8c37-681e7e089b18" alt="animated" />
</p>

> ### Interactable Dashboard
> 
> Viewing different filter options.

![interactable-1](https://github.com/user-attachments/assets/70b293d5-d460-4e48-9260-405e1c11a5cd)

![interactable-2](https://github.com/user-attachments/assets/d513c819-12d1-4b19-85dc-e353145fa676)

## Contributors

- 曾裕興 ([KenjiTECHinc](https://github.com/KenjiTECHinc))
- 彭湘淇 ([kikipeng2000](https://github.com/kikipeng2000))
- 梅夫 (Mave K. Alexander)

---

## License

This project is licensed under the [MIT License](LICENSE).
