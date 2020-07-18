#First import the necessary tests from scipy and the data (familiar)
import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

#To get the life span of subscribers of the vein pack
vein_pack_lifespans = familiar.lifespans(package='vein')

#We use the ttest_1samp To find out the significant difference of the lifesapn of the vein subsriber, from the average life span of 71 years.
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
print(vein_pack_test)

#P value of less than 0.05 proves significance
if vein_pack_test.pvalue < 0.05:
  print("The Vein Pack Is Proven To Make You Live Longer!")
else:
  print("The Vein Pack Is Probably Good For You Somehow")
artery_pack_lifespans  = familiar.lifespans(package='artery')

#We perform the ttest_ind to compare the vein pack with another product called the artery pack, to determine if there is a significant difference in the lifespan of subsribers to boths packs.
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(package_comparison_results)
if (package_comparison_results.pvalue < 0.05):
  print("the Artery Package guarantees even stronger results!")
else:
  print("the Artery Package is also a great product!")

#Since there is no significant difference, we use the Chi-Squared test to make further claims based on the results of the iron counts in the blood of the subsribers.
iron_contingency_table = familiar.iron_counts_for_package()
# Chi Squared test for iron counts
_, iron_pvalue, _, _ = chi2_contingency(iron_contingency_table)

#To get Pvalue from Chi Squared Test
print(iron_pvalue)
print("The Artery pack is proven to make you healthier")
