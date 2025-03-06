from argparse import ArgumentParser

#Create Parser
parser = ArgumentParser()

#Add Arguments
parser.add_argument("--output","-o",required=True, help ="Destination File")
parser.add_argument("--text","-t",required=True, help ="Text to Write")


#Get the Args passed to program
args = parser.parse_args()

#Write Given text to File
with open(args.output,'w') as f:
    f.write(args.text + "\n")

print(f'Wrote "{args.text}" to file {args.output}')
