
# Westbury Team 1 
## CSCI 665 NYIT Fall 2022 Simo


**Team Members** <br>
 1. Alex Gusmano	agusmano@nyit.edu	516-382-0856<br>
 2. Robert Trieste	rtrieste@nyit.edu	917-806-6333<br>
 3. Mohana Pranadeep Potti	mpotti@nyit.edu	315-737-1799<br>
 4. Pavani Gummadi pgumma01@nyit.edu	848-345-0235<br>
 5. Venkata Ratna Sandeep Paladugu	vpalad03@nyit.edu	315-737-1415<br>
 6. Rajeev Gurram	rgurra07@nyit.edu	973-641-9942<br>

- <a href="#AppHighlights">Application Highlights</a><br>
- <a href="#UseOfCloud">Use of Cloud</a><br>
- <a href="#ProjectStructure">Project Structure</a><br>
- <a href="#Backend">Backend</a><br>
- <a href="#ProjectStructure">Frontend</a><br>
- <a href="#TeamMeetings">Team Meetings</a><br>
- <a href="#Jira">JIRA</a><br>
- <a href="#Confluence">Confluence</a><br>

<p><a name="AppHighlights"></a></p>

<p><strong>Some highlights of this application:</strong></p>

<p><a name="UseOfCloud"></a></p>

<p><strong>Use of the Cloud - Touch all 3 major Cloud Platforms:</strong></p>

<ul>
  <li>We utilize <strong>infrastructure from all three major cloud providers</strong>: </li>

  <li><a href='https://aws.amazon.com/' target="_blank" rel="noopener">Amazon AWS</a>
    for the backend to host a Linux EC2 instance. </li>

  <li><a href='https://cloud.google.com/' target="_blank" rel="noopener">Google Cloud Platform (GCP)</a> service account
    to host the dataframe
    produced.</li>

  <li><a href='https://azure.microsoft.com/en-us/' target="_blank" rel="noopener">Microsoft Azure</a> to host and run
    our static web app with a
    <a href='https://learn.microsoft.com/en-us/azure/static-web-apps/build-configuration?tabs=github-actions'
      target="_blank" rel="noopener">CI/CD</a>
    pipeline through <a href='https://github.com/' target="_blank" rel="noopener">Git Hub.</a>
  </li>

<p><a name="ProjectStructure"></a></p>

<p><strong>Constructing the application:</strong></p>

  <li>Built with <a href='https://visualstudio.microsoft.com/downloads/' target="_blank" rel="noopener">Visual Studio
      Code</a> and</li>

  <li><a href='https://angular.io/' target="_blank" rel="noopener">Angular</a> utilizing <a
      href='http://www.typescriptlang.org/' target="_blank" rel="noopener">TypeScript</a> for
    client-side code.</li>

  <li>VS Code has Angular CLI integration. In development mode, there's no need to run
    <code>ng serve</code>.
    <br>It runs in the background automatically, so your client-side resources are dynamically built
    on demand and the page refreshes <br>when you modify any file.
  </li>

  <li>Efficient production builds. In production mode, development-time features are disabled, and
    your <code>dotnet publish</code> configuration <br>automatically invokes <code>ng build</code> to produce minified,
    ahead-of-time compiled JavaScript files.
  </li>

  <li><a href='http://getbootstrap.com/' target="_blank" rel="noopener">Bootstrap</a> for layout and styling.
  </li>

<p><a name="Backend"></a></p>

<p><strong>Backend:</strong></p>

  <li>The process kicks off daily with <a href='https://en.wikipedia.org/wiki/Cron' target="_blank" rel="noopener">CRON
    </a>scheduler in EC2 running <a href='https://www.python.org/' target="_blank" rel="noopener">Python</a>
    scripts that collect publicly-available gas price data published <br> by the American Automobile Association</li>

  <li>The first Python script scrapes the gas price data from the web and writes it as a CSV file to Google Sheets
    through the API with credentials.</li>

  <li>The second Python script reads that CSV into a <a href='https://wesmckinney.com/pages/about.html' target="_blank"
      rel="noopener">Pandas
      dataframe</a> and then uses the open source charting Python library <a href='https://en.wikipedia.org/wiki/Plotly'
      target="_blank" rel="noopener">Plotly</a> to create the choropleth heatmap.</li>

  <li><a href='https://pypi.org/' target="_blank" rel="noopener">Libraries</a> such as Beautiful Soup, Pandas, Pydrive,
    Google Auth, and Google Sheets
    API help accomplish all of this and
    employ the <br>software engineering concept of efficient reuse.</li>
</ul>

<p><a name="Frontend"></a></p>

<p><strong>Frontend:</strong></p>

  <li>The Plotly chart is hosted in <a href='https://chart-studio.plotly.com/feed/#/' target="_blank"
      rel="noopener">Chart-Studio</a> from where it is
    then
    embedded into our site through the Angular front end.</li>


<p><a name="TeamMeetings"></a></p>

<p><strong>Team Meetings:</strong></p>

Ran Angular Test(s)
Found Error caused by Change in title (addition of spaces)
Ex:"USAGasPriceTracker" -> "USA Gas Price Tracker"
Error is purely cosmetic and negligable when it comes to function of the code.

Also went over how the project works from FrontEnd To BackEnd

Discussed Readme Documentation as well as project FrontEnd to BackEnd Functionality
Guided Pranadeep as to how to formatt README.md

### Our team meet via Zoom video conference and used a private WhatsApp Group to schedule meetings.
 - We discussed **iterative** approach to building the project.

![img](images/Nov_TeamMeeting.png)



 