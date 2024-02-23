#lists

s3_buckets_lists = [ "sudha_demo_bucket" ,"developer_bucket" , "tester_bucket"]

print(s3_buckets_lists)
print(s3_buckets_lists[1])



s3_buckets_lists.append ("kanna_s3_bucket")

print(len(s3_buckets_lists))



s3_buckets_lists.remove ("tester_bucket")

print(s3_buckets_lists)
print(len(s3_buckets_lists))


new_list = s3_buckets_lists[0:2]
print(new_list)

numbers =[1 , 25 ,12]
numbers.sort()

print(numbers)