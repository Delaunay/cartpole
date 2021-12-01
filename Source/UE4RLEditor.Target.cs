// BSD 3-Clause License Copyright (c) 2021, Pierre Delaunay All rights reserved.

using UnrealBuildTool;
using System.Collections.Generic;

public class UE4RLEditorTarget : TargetRules
{
	public UE4RLEditorTarget( TargetInfo Target) : base(Target)
	{
		Type = TargetType.Editor;
		DefaultBuildSettings = BuildSettingsVersion.V2;
		ExtraModuleNames.AddRange( new string[] { "UE4RL", "AIModule" } );
	}
}
