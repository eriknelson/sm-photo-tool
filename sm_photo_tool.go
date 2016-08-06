/*
 * sm_photo_tool.go - update and create smugmug galleries from the
 *                    command line
 *
 * Copyright (C) 2016 Jesus M. Rodriguez
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
 */

package main

import (
	"fmt"
	"os"

	"github.com/pborman/getopt"
)

func main() {
	//CLI{}.run()
	optName := getopt.StringLong("name", 'n', "", "Your name")
	optHelp := getopt.BoolLong("help", 0, "Help")

	getopt.Parse()
	args := getopt.Args()

	if *optHelp {
		getopt.Usage()
		os.Exit(0)
	}

	fmt.Println("Hello " + *optName + "!")
	validOptions := []string{"album", "galleries"}
	lcmd := ListCommand{usage: "Usage", desc: "the list command", valid_options: validOptions}
	lcmd.Go(args)
	fmt.Println("Did doCommand get called?")
}
