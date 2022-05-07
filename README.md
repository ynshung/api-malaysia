# api-malaysia

Historical data of the Air Pollution Index (API, [wiki](https://en.wikipedia.org/wiki/Air_Pollution_Index)) in Malaysia from 2005 to 2017 with web scraping script.

## Notes

1. Some location may not be available such as the three mobile continuous air quality monitoring station (MCAQM) in Malaysia as its history is not saved in the website.
2. There are some monitoring station that used to be turned on and now discontinued or vice versa.
3. There are a few dates that the API failed to retrieve data.
4. The web scraping script could be improved further.
5. Retrieved data is saved under the cache folder. You can unpack the archive to save some time.

## TODO
* ✅ Rewrite web scraping script to continue from current file.
* Write instructions on how to run script

## Sources and Licensing

Data from 2005 to 2017 are retrieved from [data.gov.my](http://www.data.gov.my/) under MOSTI, DOE and KeTSA. The data is licensed under [Creative Commons Attribution](https://opendefinition.org/licenses/cc-by/) and [Open Definition 2.1](https://opendefinition.org/od/2.1/en/).

The data from 2018 to current date are retrieved directly from [APIMS](http://apims.doe.gov.my/public_v2/api_table.html) website. Data might still be under copyright (unclear) but it's *safe to assume* the data will eventually be released under the same license as above.

The web scraping script is licensed under MIT.
