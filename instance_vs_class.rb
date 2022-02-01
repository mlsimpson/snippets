class C
	puts "Just inside class definition block. Here's self:"
	p self
	@v = "I am an instance variable at the top level of a class body."
	puts "And here's the instance variable @v, belonging to #{self}:"
	p @v
  # this is a class function
	def show_var
		puts "Inside an instance method definition block. Here's self:"
		p self
		puts "And here's the instance variable @v, belonging to #{self}:"
    # class variable! not part of the "c" instance!
		p @v
	end
end
c = C.new
c.show_var
