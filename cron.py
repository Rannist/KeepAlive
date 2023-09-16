import yaml, random, uuid, os, datetime

def is_prime_number(number: int) -> bool:
  if number <= 1:
    return False
  for i in range(2, int(number / 2) + 1):
    if (number % i) == 0:
      return False
  else:
    return True

# skip if day of month is a prime number
day = int(datetime.datetime.now().strftime("%d"))
if (is_prime_number(day)):
  print("Skipped because day of month is a prime number.")
  exit(0)

# default action yaml path & test file path
#yaml_path = ".github/workflows/commit.yml"
test_path = "test.java"

# load yaml to object yml
#yml = yaml.safe_load(open(yaml_path))

# convert `True` to `on`
#data = {key if key != True else "on": yml[key] for key in yml}

# random min & hour number
#min = random.randint(0, 59)
#hour = random.randint(0, 2)

# randomly edit cron
#cron = f"{min} {('*/' + str(hour)) if hour != 0 else '*'} * * *"
#data["on"]["schedule"][0]["cron"] = cron
#print(f"Rewrite cron to `{cron}`")

# rewrite the action file
#os.remove(yaml_path)
#yaml.dump(data, open(yaml_path, "w"))

# get random uuid
random_uuid = uuid.uuid4()

# randomly edit the content of test.java
with open(test_path, "r+") as test:
  test.write(str(random_uuid))
print(f"Rewrite test file to `{random_uuid}`")

# all done
print("GGs! :)")
