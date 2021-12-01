// BSD 3-Clause License Copyright (c) 2021, Pierre Delaunay All rights reserved.

using UnrealBuildTool;
using System.Collections.Generic;

public class UE4RLTarget : TargetRules
{
	public UE4RLTarget( TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;
		DefaultBuildSettings = BuildSettingsVersion.V2;
		ExtraModuleNames.AddRange( new string[] { "UE4RL", "AIModule" } );
	}
}
  