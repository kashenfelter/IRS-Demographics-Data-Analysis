# Share my story about working with Intuit data challenge

## 1. Try to find a way

### Goal: connect the two dataset!
At the beginning, what I get is two dataset and one README. After freaking out by all the tax term inside the dataset irs_public_data.csv (short as irs-data), I tried to both understanding all the columns(for both dataset) and also think about how to connected these two datasets together to get further insight.

### Crawl for new data -- detour but still worth it!
As there are slightly different between ZCTA and zipcode(columns that could link two datasets together), which gets me confused. I tried to find data that could link these two, but failed. I didn't give up(cause at that time, I think this is the only way to link these two datasets,and I think this is really important),and compromised to find both ZCTA and zipcode that can link to STATE number. In order to accomplish this task, I crawled data from wikipedia that help me connect the state number to state name(for visualization reason). It turns out that this didn't help much with build up a model as I expected( at the end I didn't used state-grouped data), but it's good to help with visualize data.

## 2. Find the interesting question and visualize data!

### Question esteblished and its assumptions
As I further familiar with the data, I found the column num_paid_preparer_returns(short as paid-number) in irs-data interested me most.  I want to know, what's the feature of people who are willing to pay for tax return. This is based on the assumption that people whether are willing to pay for tax return or not can make a difference on their expectation to out product.

### Visualize data
After cleaning the dataset, I tried to plot paid-number together with other data. It's interesting to find out that in terms of absolute number, more people with lower income pay for tax return, while in terms of percentage, rich people are more likely to pay for tax returns.

However, this didn't satisfy me because is it too exausted and fragmented to plot all other columns with it. I decide to use regression model to find out what influence people to decide whether pay for the tax return or not.

## Let's build a regression model!

At first, I tried to built up model with data grouped by states. But when I found that CA, TX, NY, are influencial points of the model, I realise grouped data is not going to work. I can not build up a useful model without these three important states! And I simply switch to ungrouped data.

## 4. Conclusion and future
I found column Old.age.dependency.ratio is interesting. it suggests that as the older people become more, it is more likely to spend money on this. Our survice that need user to pay should focus more on older people and places that 
