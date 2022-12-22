def sparse_search(data, search_val):
  print("Data: " + str(data))
  print("Search Value: " + str(search_val))
  first, last = 0, len(data) - 1 #variables equal to the first and last positions of dataset
  while first <= last:       #iterating until we find our search value
    mid = (first + last) // 2     
    if not data[mid] :        #check if the middle is empty
      left, right = mid - 1, mid + 1
      while True:       # checking if the surrounding values are empty
        if left < first and right > last:  #check if the middle is empty
            print(str(search_val)+ ' is not in the dataset')
            return
        elif right <= last and data[right]:   #check the value to the right
          mid = right
          break
        elif left >= first and data[left]:    #check the value of the left
          mid = left
          break
        right += 1   #move our pointers
        left -= 1
    
    if data[mid] == search_val:     #if the middle of the data is equal to our search value
      print(str(search_val) + ' found at position '+ str(mid))
      return
    elif search_val < data[mid]:  #check if the Search Value is Less Than the Middle
      last = mid - 1
    elif search_val > data[mid]:  #check if the Search Value is Greater Than the Middle
      first = mid + 1
  print(str(search_val) + ' is not in the dataset') #value not in data


