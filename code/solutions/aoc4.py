import re

# manually loaded the input into a variable called "all_passports"
input = """<copy_paste"""
all_passports = input.split('\n\n')

### part one (copied into ipython)
valid = 0
fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

for passport in all_passports:
	necessary = fields.copy()
	input_fields = re.split('[\s\n]+', passport)
	for field in input_fields:
		code, code_val = field.split(':')
		if code in necessary:
			necessary.remove(code)
			
	if len(necessary) == 0:
		valid += 1

print(valid)


### part two (copied into ipython)
valid = 0
fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

for passport in all_passports:
	necessary = fields.copy()
	input_fields = re.split('[\s\n]+', passport)
	for field in input_fields:
		code, code_val = field.split(':')
		if code in necessary:
			# lol, copypasta 4tw
			if ((code == 'byr' and 1920 <= int(code_val) and int(code_val) <= 2002) or
					(code == 'iyr' and 2010 <= int(code_val) and int(code_val) <= 2020) or
					(code == 'eyr' and 2020 <= int(code_val) and int(code_val) <= 2030)):
				if len(code_val) == 4:
					necessary.remove(code)
			elif code == 'hgt':
				cm = re.match('^(\d+)cm$', code_val)
				if cm:
					cm_val = int(cm.groups()[0])
					if 150 <= cm_val and cm_val <= 193:
						necessary.remove(code)
				inches = re.match('^(\d+)in$', code_val)
				if inches:
					in_val = int(inches.groups()[0])
					if 59 <= in_val and in_val <= 76:
						necessary.remove(code)
			elif code == 'hcl':
				hcl_match = re.match('^#[0-9a-f]{6}$', code_val)
				if hcl_match:
					necessary.remove(code)
			elif code == 'ecl' and code_val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
				necessary.remove(code)
			elif code == 'pid' and len(code_val) == 9:
				pid_match = re.match('^[0-9]{9}$', code_val)
				if pid_match:
					necessary.remove(code)
			
			if code in necessary and code in ['hgt','hcl']:
				print(f"{code}:{code_val} was invalid")
	
	if len(necessary) == 0:
		valid += 1

print(valid)