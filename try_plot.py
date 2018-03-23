import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000)


# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

# # add a 'best fit' line
# y = mlab.normpdf( bins, mu, sigma)
# l = plt.plot(bins, y, 'r--', linewidth=1)
#
# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)

#plt.show()




irs_public = 'irs_public_data.csv'
acs_population = 'acs_population_demographics.csv'

def read_file(file):
    str_list = []
    f = open(file, 'r')
    title = f.readline()[:-2].split(',')
    print(title)
    next(f)
    for l in f.readlines():
        l=l[:-2]
        str_list.append(l.split(","))

    f.close()
    return title,str_list

# turn irs data into python object
pub_title , pub_list_data= read_file(irs_public)
pub_data = np.asarray(pub_list_data)
sub_data = pub_data[:,0]



def plot_statistics(key, index,all_stats):
    color = ['red','blue','green','black','brown']
    f, ax = plt.subplots()
    ax.set_title(key)
    for i in range(len(index)):
        ax.plot(all_stats[:,index[i]], color=color[i])

    f.savefig(key+'.png')

# try plot the raw data of irs data

# conf1, conf2 = conference_keys
index = [3]
plot_statistics('num of returns',index,pub_data)



def plot(y,num_steps,step):
    # range1 = lambda start, end: range(start, end + 1)
    x = []
    for i in range(0, num_steps, step):
        x.append(i)
    #create the instance
    plt.figure(figsize=(8, 4))
    # configuration
    plt.plot(x, y, "b--", linewidth=1)
    #labels
    plt.xlabel("Number Of Steps")
    plt.ylabel("Log Likelihood")
    #title of the plot
    plt.title("Logistic regression's behavior over time")
    # show file
    plt.show()
    # save file
    plt.savefig("line.png")
    print('Finish plot the data!')


#
#
# plot_statistics('author_conference_happiness', conf1.id, conf2.id, all_stats, take_mean=True)
# plot_statistics('reviewer_quality_assessments', conf1.id, conf2.id, all_stats, take_mean=True)
# plot_statistics('num_reviewers', conf1.id, conf2.id, all_stats)
# plot_statistics('num_submitted', conf1.id, conf2.id, all_stats)
# plot_statistics('percent_accepted', conf1.id, conf2.id, all_stats)
# plot_statistics('paper_true_quality', conf1.id, conf2.id, all_stats)