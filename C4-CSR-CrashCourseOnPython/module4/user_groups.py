def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for groups in group_dictionary:
		# Now go through the users in the group
		for user in group_dictionary[groups]:
			# Now add the group to the the list of
			if user not in user_groups:
				user_groups[user] = [groups]
				continue
			user_groups[user].append(groups)

# groups for this user, creating the entry
# in the dictionary if necessary
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for groups in group_dictionary:
		# Now go through the users in the group
		for user in group_dictionary[groups]:
			# Now add the group to the the list of
			if user not in user_groups:
				user_groups[user] = [groups]
			else:
				user_groups[user].append(groups)
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))